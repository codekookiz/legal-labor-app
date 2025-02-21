import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json
from huggingface_hub import InferenceClient  # HF Inference API 사용
from datetime import date, datetime, timedelta

def run_del():
    def get_huggingface_token():
        token = os.environ.get('HUGGINGFACE_API_TOKEN')
        if token is None:
            token = st.secrets.get('HUGGINGFACE_API_TOKEN')
        return token
    
    def get_google_credentials():
        token = os.environ.get('GOOGLE_CREDENTIALS')
        if token is None:
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

    valid = False

    # 사용자 입력 받기
    st.subheader("기본 정보")
    name = st.text_input("이름", key="name_del", help="상담을 예약한 분의 이름을 입력하세요.")
    phone = st.text_input("연락처", key="phone_del", help="상담을 예약한 분의 연락처를 입력하세요.")

    st.subheader("상담 예약 정보")
    sel_date = st.date_input("상담 날짜", value=date.today() + timedelta(days=1), key="date_del", help="상담을 예약한 날짜를 선택하세요.")
    times = [f"{hour:02d}:00" for hour in [10, 11, 13, 14, 15, 16, 17]]
    time = st.selectbox("상담 시간", times, key="time_del", help="상담을 예약한 시간을 선택하세요.")
    new_date = sel_date.strftime("%Y-%m-%d") + " " + time
    new_date = datetime.strptime(new_date, "%Y-%m-%d %H:%M")

    if st.button("상담 취소"):
        if name and phone and sel_date and time:
            if new_date > datetime.now():
                valid = True
            if valid:
                st.markdown("### 상담 취소 처리 중...")
                # 기존 신청한 상담 존재하는지 확인
                records = sheet.get_all_records()
                matching_rows = [
                    row for row in records
                    if row['이름'] == name and row['연락처'] == phone and row['날짜'] == str(sel_date) and row['시간'] == time
                ]
                if not matching_rows:
                    st.error("해당 시간에 예약된 상담이 없습니다. 입력 정보를 다시 확인해주세요.")
                else:
                    # Google Sheets에서 matching_rows와 같은 데이터 삭제
                    for row in matching_rows:
                        sheet.delete_rows(records.index(row) + 2)
                    st.success("상담 예약이 취소되었습니다.")
            else:
                st.error("이미 지난 시간은 선택할 수 없습니다.")
        else:
            st.error("모든 필드를 입력해주세요!")