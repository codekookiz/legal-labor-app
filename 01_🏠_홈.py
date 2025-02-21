import streamlit as st

st.markdown(
    """
    <h1 style='text-align: center; color: #4C82C2;'>
        ⚖️ 노동법 관련 컨설팅 앱
    </h1>
    <h2 style='text-align: center; color: #4C82C2;'>
        🤖 딥러닝 기반
    </h2>
    """, unsafe_allow_html=True
)

# 사이드바 메뉴
st.sidebar.title("")

st.text('')
st.text('')

# 제목
st.markdown(
    """
    <h2 style="text-align: center; color: #FF4B4B;">
        노동법 상담 및 정보 제공 서비스 개요
    </h2>
    """, 
    unsafe_allow_html=True
)

# 설명
st.markdown(
    """
    <p style="font-size: 18px; text-align: center;">
        🧑‍⚖️ 본 서비스는 노동법 분야의 변호사가 직접 상담 및 정보를 제공하는 서비스입니다.<br>
        노동법 분야의 다양한 문제에 대해 전문가의 조언을 받아보세요.
    </p>
    """, 
    unsafe_allow_html=True
)

st.markdown("---")

# 📌 데이터 출처 및 구성
st.markdown("### 📌 **사용 데이터**")
st.info(
    """
    🔹 **[법률 상담 요청.gsheets](https://docs.google.com/spreadsheets/d/1p9CvCU8zX8rALM9rwYqbnFNZsq3wHQzvWJz2-iVh1f0/edit?usp=sharing)**  
    * **상담 신청된 데이터를 저장**하는 데이터셋입니다.\n\n 
    * 상담 신청자의 정보와 문의 내용뿐만 아니라 문의 내용을 기반으로 분류된 **카테고리**, **담당 변호사명**을 저장합니다.
    """
)

st.markdown("---")

# 이미지 추가
# st.image("image/main_home.png", use_container_width=True)

st.markdown("---")

# ⚡ 기능 소개
st.markdown("### ⚡ **탭별 주요 기능**")
st.markdown(
    """
    - ℹ 앱 정보: 앱의 소개와 활용 예시, 개발 정보 등을 확인할 수 있습니다.
    - ⚒️ 개발 정보: 앱 개발에 사용된 기술 스택, 데이터 출처 등을 확인할 수 있습니다.
    - 📜 상담 예약: 상담을 희망하는 이용자가 정보를 입력하면 상담 예약을 진행합니다.
    - 🧭 조회 및 변경: 접수된 상담 예약 정보를 기반으로 상담 조회, 변경 및 취소가 가능합니다.
    - 💬 챗봇: 노동 및 근로 분야의 질문에 답하는 챗봇 WorkBot을 사용할 수 있습니다.
    """
)

st.markdown("---")

# 📢 활용 예시
st.markdown("### 📢 **이렇게 활용할 수 있어요!**")
st.markdown(
    """
    - 👤 **사용자**:
        - 비교적 알기 어려운 노동법 관련 분야에 대한 상세한 상담을 진행할 수 있습니다.
        - 챗봇을 통해 빠르고 간편하게 질문에 대한 답변을 받을 수 있습니다.
        - 상담 예약 시스템을 통해 편리하게 상담 일정을 잡을 수 있습니다.
    - 🧑‍⚖️ **변호사**:
        - 상담 예약을 통해 사용자의 상담 요청을 확인하고, 상담 내용을 기반으로 상세한 답변을 제공할 수 있습니다.
        - 상담 내역을 관리하고, 필요 시 상담 일정을 변경하거나 취소할 수 있습니다.
        - 챗봇을 통해 자주 묻는 질문에 대한 답변을 자동화하여 효율성을 높일 수 있습니다.
    - 📈 **관리자**:
        - 상담 예약 정보를 확인하고, 변경 및 취소를 관리할 수 있습니다.
        - 상담 데이터를 분석하여 서비스 개선에 활용할 수 있습니다.
        - 사용자와 변호사 간의 상담 내역을 모니터링하고, 원활한 상담 진행을 지원할 수 있습니다.
    """
)

st.markdown("---")

