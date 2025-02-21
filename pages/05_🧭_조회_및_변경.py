import streamlit as st

from ui.delete import run_del
from ui.status import run_status
from ui.update import run_up

st.markdown(
    """
    <style>
    .title {
        font-size: 36px;
        color: #4C82C2;
        text-align: center;
    }
    .header {
        font-size: 28px;
        color: #4C82C2;
        text-align: center;
    }
    .subheader {
        font-size: 24px;
        color: #4C82C2;
    }
    .text {
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown("<h1 class='title'>📜 상담 내역 조회 및 수정</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='header'>상담 내역을 조회, 변경 및 취소할 수 있습니다.</h2>", unsafe_allow_html=True)

# 탭 생성
tab1, tab2, tab3 = st.tabs(["예약 정보 조회", "예약 정보 변경", "상담 예약 취소"])

with tab1:
    st.markdown("<h3 class='subheader'>예약 정보 조회</h3>", unsafe_allow_html=True)
    st.markdown("<p class='text'>예약된 상담 정보를 조회할 수 있습니다. 이름과 연락처를 입력하여 예약 정보를 확인하세요.</p>", unsafe_allow_html=True)
    run_status()

with tab2:
    st.markdown("<h3 class='subheader'>예약 정보 변경</h3>", unsafe_allow_html=True)
    st.markdown("<p class='text'>예약된 상담 정보를 변경할 수 있습니다. 이름과 연락처를 입력하여 예약 정보를 확인하고, 변경할 내용을 입력하세요.</p>", unsafe_allow_html=True)
    run_up()  # 상담 일정 변경 함수 실행

with tab3:
    st.markdown("<h3 class='subheader'>상담 예약 취소</h3>", unsafe_allow_html=True)
    st.markdown("<p class='text'>예약된 상담을 취소할 수 있습니다. 이름과 연락처를 입력하여 예약 정보를 확인하고, 취소할 상담을 선택하세요.</p>", unsafe_allow_html=True)
    run_del()  # 상담 취소 함수 실행