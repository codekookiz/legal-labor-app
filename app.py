import streamlit as st

from ui.consult import run_consult
from ui.home import run_home
from ui.chat import run_chat
from ui.up_del import run_up_del


def main():
    
    st.markdown(
        """
        <h1 style='text-align: center; color: color: #4C82C2;'>
            ⚖️ 노동법 관련 컨설팅 앱
        </h1>
        <h2 style='text-align: center; 'color: #4C82C2;'>
            🤖 딥러닝 기반
        </h2>
        """, unsafe_allow_html=True
    )

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🏠 홈", "ℹ 앱 상세 정보", "⚒️ 개발 정보", "📜 상담 예약", "상담 변경 및 취소", "💬 챗봇"])

    # 각 탭에 해당하는 기능 실행
    with tab1:
        run_home()

    #with tab2:
        #run_info()

    # with tab3:
    #     run_dev()

    with tab4:
        run_consult()

    with tab5:
        run_up_del()

    with tab6:
        run_chat()


if __name__ == "__main__":
    main()