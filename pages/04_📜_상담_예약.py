import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json
from huggingface_hub import InferenceClient  # HF Inference API 사용
from datetime import date, datetime, timedelta


def get_huggingface_token() :
    token = os.environ.get('HUGGINGFACE_API_TOKEN')
    if token is None :
        token = st.secrets.get('HUGGINGFACE_API_TOKEN')
    return token

def get_google_credentials() :
    token = os.environ.get('GOOGLE_CREDENTIALS')
    if token is None :
        token = st.secrets.get('GOOGLE_CREDENTIALS')
    return json.loads(token)

google_cred = get_google_credentials()

# Google Sheets API 설정
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(google_cred, scope)
client = gspread.authorize(creds)

# Google Sheets 열기
sheet = client.open("법률 상담 요청").sheet1

# Hugging Face Inference API 설정
HF_API_TOKEN = get_huggingface_token()  # 환경 변수 또는 Streamlit 비밀 변수에서 HF 토큰 가져오기
client = InferenceClient(token=HF_API_TOKEN)

# 변호사 매칭 데이터
lawyers = {
    "근로계약 및 해고 문제": ["김철수 변호사", "이민호 변호사"],
    "임금 체불 및 연장근로": ["이영희 변호사", "박지수 변호사"],
    "퇴직금 및 휴가 문제": ["최성호 변호사", "김민지 변호사"],
    "산업재해 및 산재 보상": ["박민준 변호사", "이지은 변호사"],
    "직장 내 괴롭힘 및 차별": ["최지훈 변호사", "박지현 변호사"]
}

# 상담 카테고리 목록
categories = list(lawyers.keys())

# Streamlit UI
st.title("📜 상담 예약 시스템")
st.header("법률 상담 예약을 위한 정보를 입력하세요.")
st.text("아래 양식을 작성하여 상담 예약을 진행해주세요.")

valid = False

# 사용자 입력 받기
st.subheader("기본 정보")
name = st.text_input("이름", help="상담을 예약할 분의 이름을 입력하세요.")
phone = st.text_input("연락처", help="상담을 예약할 분의 연락처를 입력하세요.")

st.subheader("상담 예약 정보")
sel_date = st.date_input("상담 날짜", value=date.today() + timedelta(days=1), help="상담을 원하는 날짜를 선택하세요.")
times = [f"{hour:02d}:00" for hour in [10, 11, 13, 14, 15, 16, 17]]
time = st.selectbox("상담 시간", times, help="상담을 원하는 시간을 선택하세요.")
new_date = sel_date.strftime("%Y-%m-%d") + " " + time
new_date = datetime.strptime(new_date, "%Y-%m-%d %H:%M")

st.subheader("상담 요청 내용")
issue = st.text_area("상담 요청 내용", help="상담을 원하는 내용을 상세히 입력하세요.")

if st.button("상담 요청 접수"):
    if name and phone and sel_date and time and issue:
        if new_date > datetime.now():
            valid = True
        if valid:
            st.markdown("### 상담 요청 처리 중...")
            # AI 모델로 상담 카테고리 분류
            classification = client.post(
                model="facebook/bart-large-mnli",
                json={"inputs": issue, "parameters": {"candidate_labels": categories}}
            )
            category = json.loads(classification.decode("utf-8"))["labels"][0]  # 가장 확신이 높은 카테고리 선택
            lawyer_list = lawyers.get(category)

            # 해당 날짜 해당 시간에 해당 변호사의 상담이 이미 예약되어 있는지 확인
            records = sheet.get_all_records()  # 시트 데이터를 가져옴
            for lawyer in lawyer_list:
                matching_rows = [
                    row for row in records
                    if row['날짜'] == str(sel_date) and row['시간'] == time and row['변호사명'] == lawyer
                ]
                if not matching_rows:
                    lawyer = lawyer
                    break
            if matching_rows:
                st.error("해당 시간에 예약된 상담이 존재합니다. 다른 시간을 선택해주세요.")
            else:
                # Google Sheets에 저장
                sheet.append_row([name, phone, str(sel_date), str(time), issue, category, lawyer])
                # 결과 출력
                st.success(
                    f"✅ **{category}** 관련 사안에 대해 문의 주셨습니다.\n\n"
                    f"📅 **{sel_date} {time}**로 상담 예약이 완료되었습니다.\n\n"
                    f"👨‍⚖️ 담당 변호사 : **{lawyer}**"
                )
        else:
            st.error("이미 지난 시간은 선택할 수 없습니다.")
    else:
        st.error("모든 필드를 입력해주세요!")