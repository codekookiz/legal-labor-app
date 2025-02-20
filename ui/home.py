import streamlit as st

def run_home():

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
            💵 2014년부터 10년 간의 물가 데이터를 기반으로 <b>미래의 물가를 예측</b>하는 앱입니다!<br>
            데이터 시각화와 머신러닝 모델을 활용하여 <b>과거와 미래의 물가 수준을 직접 확인해보세요.</b>
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
        * 상담 신청자의 정보와 문의 내용뿐만 아니라 문의 내용을 기반으로 분류된 **카테고리**, **담당 변호사명**을 저장합니다.\n\n
        🔹 **price_level_index.csv** (상단 데이터 .csv 변환 및 일부 수정)\n\n
        * 식료품 관련 데이터만 사용할 계획이므로 **불필요 데이터**('교통', '통신' 등 컬럼) 제거\n\n
        * 각 컬럼명 앞에 붙은 **공백 제거** 및 '계정항목' 컬럼의 데이터 타입을 **날짜 데이터**로 변환
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
        - ℹ 앱 상세 정보: 물가 예측 모델과 활용 방법에 대한 상세 설명 제공
        - ⚒️ 개발 정보: 앱 개발 과정과 사용된 기술 스택 소개
        - 📊 과거 물가 비교하기: 특정 항목의 과거 물가 변동을 시각적으로 분석
        - 🍚 식료품 물가 예측하기: AI 모델이 입력한 날짜를 기준으로 예상 물가를 예측
        """
    )

    st.markdown("---")

    # 📢 활용 예시
    st.markdown("### 📢 **이렇게 활용할 수 있어요!**")
    st.markdown(
        """
        - 🏢 기업 및 자영업자 → 원자재 및 운영 비용 상승을 예측하여 미리 대비  
        - 👨‍👩‍👧‍👦 소비자 → 생활 필수품 가격 변동을 예측하여 합리적인 소비 계획 수립  
        - 📊 연구자 및 경제 분석가 → 과거 데이터를 기반으로 경제 흐름을 분석 및 연구
        """
    )

    st.markdown("---")