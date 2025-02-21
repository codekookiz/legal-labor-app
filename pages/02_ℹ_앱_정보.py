import streamlit as st

def run_info():

    st.text('')
    st.text('')

    st.markdown(
        """
        <h2 style="text-align: center; color: #FF4B4B; font-family: 'Arial', sans-serif;">
            ℹ 앱 상세 정보
        </h2>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        """
        <h3 style="font-size: 26px; color: #333; font-family: 'Arial', sans-serif;">
            앱 개요
        </h3>
        <p style="font-size: 18px; line-height: 1.8; letter-spacing: 0.5px; color: #555;">
        스타벅스 음료 데이터를 기반으로 사용자들의 음료 주문 현황 데이터를 수집하고
        이를 분석하여 딥러닝 모델을 통해 사용자들에게 음료를 추천하는 앱입니다.

        <p style="font-size: 18px; line-height: 1.8; letter-spacing: 0.5px; color: #555;">
        📊 사용자들의 주문 데이터를 분석하여 사용자 선호도를 파악하고, 이를 바탕으로 사용자에게 최적의 음료를 추천합니다.
        </p>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("---")

    # 예상 이용자
    st.markdown(
        """
        <h3 style="font-size: 26px; color: #333; font-family: 'Arial', sans-serif;">
            예상 이용자
        </h3>
        <br> 
        <ul style="font-size: 18px; line-height: 1.8; color: #555;">
            <li><b>👤 스타벅스 고객</b>: 다양한 음료의 영양정보를 확인하고, 자신의 취향에 맞는 음료를 추천받고자 하는 고객.</li>
            <li><b>💪 헬스 컨셔스 고객</b>: 음료의 칼로리와 영양정보를 확인하여 건강한 선택을 하고자 하는 고객.</li>
            <li><b>🏢 스타벅스 매장 관리자</b>: 고객의 주문 데이터를 분석하여 매장 운영과 마케팅 전략을 개선하고자 하는 관리자.</li>
            <li><b>📊 데이터 분석가</b>: 음료 주문 데이터를 분석하여 트렌드를 파악하고, 새로운 인사이트를 도출하고자 하는 분석가.</li>
        </ul>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("---")

    # 앱의 장점
    st.markdown(
    """
    <h3 style="font-size: 26px; color: #333; font-family: 'Arial', sans-serif;">
        앱의 장점
    </h3>
    <br>
    <ul style="font-size: 18px; line-height: 1.8; color: #555;">
        <li><b>🎯 맞춤형 추천</b>: 사용자의 주문 데이터를 분석하여 개인 맞춤형 음료를 추천합니다.</li>
        <li><b>🍃 영양정보 제공</b>: 다양한 음료의 영양정보를 제공하여 건강한 선택을 도와줍니다.</li>
        <li><b>📈 데이터 기반 통계</b>: 주문 데이터를 분석하여 전반적인 주문 경향성을 파악하고, 이를 통계화할 수 있습니다.</li>
        <li><b>🎨 사용자 친화적 인터페이스</b>: 직관적이고 사용하기 쉬운 인터페이스를 제공합니다.</li>
        <li><b>🔍 다양한 활용 가능성</b>: 고객, 매장 관리자, 데이터 분석가 등 다양한 이용자에게 유용한 정보를 제공합니다.</li>
    </ul>
    """, 
    unsafe_allow_html=True
)

    st.markdown("---")

    st.markdown(
    """
    <h3 style="font-size: 26px; color: #333; font-family: 'Arial', sans-serif;">
        배포 과정
    </h3><br>

    <p style="font-size: 18px; line-height: 1.8; letter-spacing: 0.5px; color: #555;">
        📤 앱은 Streamlit을 사용하여 웹 애플리케이션 형태로 배포되었습니다.<br>

    <p style="font-size: 18px; line-height: 1.8; letter-spacing: 0.5px; color: #555;">
        🖥️ 초기에는 로컬 환경에서 테스트 후, requirements.txt 파일을 생성하여 외부 환경에서도 실행 가능하도록 설정하였습니다.
    </p>
    """, 
    unsafe_allow_html=True
)

    st.markdown("---")