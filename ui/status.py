import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json
from huggingface_hub import InferenceClient  # HF Inference API 사용
from datetime import date, datetime, timedelta


def run_status():
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

    valid = False

    # 사용자 입력 받기
    st.subheader("기본 정보")
    name = st.text_input("이름", key="name_status", help="상담을 예약한 분의 이름을 입력하세요.")
    phone = st.text_input("연락처", key="phone_status", help="상담을 예약한 분의 연락처를 입력하세요.")

    if st.button("예약 정보 조회"):
        if name and phone:
            # 기존 신청한 상담 존재하는지 확인
            records = sheet.get_all_records()
            matching_rows = [
                row for row in records
                if row['이름'] == name and row['연락처'] == phone
            ]
            if not matching_rows:
                st.error("예정된 상담이 없습니다. 입력 정보를 다시 확인해주세요.")
            else:
                # 다가오는 순서로 정렬하여 출력
                current_time = datetime.now()
                upcoming_rows = [
                    row for row in matching_rows
                    if datetime.strptime(f"{row['날짜']} {row['시간']}", "%Y-%m-%d %H:%M") > current_time
                ]
                if not upcoming_rows:
                    st.error("예정된 상담이 없습니다. 입력 정보를 다시 확인해주세요.")
                else:
                    # 다가오는 순서로 정렬하여 출력
                    upcoming_rows = sorted(upcoming_rows, key=lambda row: datetime.strptime(f"{row['날짜']} {row['시간']}", "%Y-%m-%d %H:%M"))
                    st.markdown(f"### 예정된 상담이 {len(upcoming_rows)}건 있습니다.")
                    for row in upcoming_rows:
                        date = row['날짜']
                        time = row['시간']
                        request = row['요청']
                        lawyer = row['변호사명']
                        st.success(
                            f"**{name}**님,\n\n"
                            f"**{date} {time}**에\n\n"
                            f"**{lawyer} 변호사**와 상담이 예약되어 있습니다.\n\n"
                            "상담 요청 내용 : \n\n"
                            f"**'{request}'**"
                        )
        else:
            st.error("모든 필드를 입력해주세요!")