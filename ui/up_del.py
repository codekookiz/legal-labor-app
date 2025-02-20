import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json
from huggingface_hub import InferenceClient  # HF Inference API 사용
from datetime import date, datetime, timedelta

from ui.delete import run_del
from ui.update import run_up


def run_up_del():

    # Streamlit UI
    st.title("📜 상담 예약 시스템")
    st.write("상담 정보를 입력하세요.")

    # 상담 취소
    # if st.button("상담 취소"):
    run_del()        

    st.header("")
    st.header("")
    st.header("")
    st.header("")

    # 상담 예약 변경
    # if st.button("상담 일정 변경"):
    run_up()
        