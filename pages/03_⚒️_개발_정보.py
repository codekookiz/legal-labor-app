import streamlit as st
import pandas as pd

def run_dev():
    # 스타일 적용
    st.markdown(
        """
        <style>
            h1, h2, h3 {
                text-align: center;
                color: #FF4B4B;
                font-family: 'Arial', sans-serif;
                display: inline-block;
                width: 100%;
            }
            h1 { font-size: 36px; font-weight: bold; }
            h2 { font-size: 30px; font-weight: bold; }
            h3 { font-size: 26px; font-weight: bold; }
            
            h2::after {
                content: "";
                display: block;
                width: 50%;
                height: 3px;
                background: #FF4B4B;
                margin: 5px auto;
                border-radius: 5px;
            }
            .highlight { color: #FF4B4B; font-weight: bold; }
            .emoji { font-size: 24px; }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 제목
    st.text('')
    st.text('')

    st.markdown(
        """
        <h2 style="text-align: center; color: #FF4B4B; font-family: 'Arial', sans-serif;">
            🛠️ 개발 정보
        </h2>
        """, 
        unsafe_allow_html=True
    )


    st.markdown("---")
    

    st.markdown('<h2>📌 프로젝트 개요</h2>', unsafe_allow_html=True)
    st.write("""
    스타벅스 음료 데이터를 기반으로 사용자들의 음료 주문 현황 데이터를 수집하고
    이를 분석하여 딥러닝 모델을 통해 사용자들에게 음료를 추천하는 앱을 개발했습니다.
    """)
    
    st.markdown('<h4>✅ 프로젝트 목표</h4>', unsafe_allow_html=True)
    st.write("""
    - **데이터 수집:** 사용자의 음료 주문 데이터를 수집하고 정제
    - **데이터 분석:** 사용자의 주문 데이터를 분석하여 사용자 선호도 파악
    - **딥러닝 모델:** 특정 사용자 및 전체 사용자의 음료 주문 경향성을 기반으로 음료 추천
    - **리뷰 시스템:** 사용자들이 구매한 음료에 대해 리뷰를 작성하고 이를 차후 음료 추천에 반영
    """)


    st.markdown("---")
    

    st.markdown('<h2>📈 데이터 수집 및 전처리</h2>', unsafe_allow_html=True)
    
    st.markdown('<h4>📌 사용한 데이터</h4>', unsafe_allow_html=True)
    st.write("""
    - **출처:** [스타벅스 코리아](https://www.starbucks.co.kr/menu/drink_list.do), [Kaggle](https://www.kaggle.com/datasets/noorunnishabegum1996/starbucks-drinkmenu-expanded)
        - 실사용 데이터셋 : 스타벅스 영양성분.csv (스타벅스 코리아 홈페이지 및 앱 내 데이터 이용하여 직접 제작)
    - **주요 특성:** 음료 유형, 음료명, 영양정보 등
    """)
    
    st.markdown('<h4>📌 전처리 과정</h4>', unsafe_allow_html=True)
    st.write("""
    - 🔹 영문 데이터 한글화: 원본 데이터셋이 미국 스타벅스의 음료 정보 기반으로 생성
        - 한국 스타벅스의 음료 정보에 따라 컬럼 및 데이터명 번역
             - 예시: "Beverage" -> "음료명"
    - 🔹 한국 스타벅스 메뉴 데이터 추가:
        - 미국 스타벅스에 존재하지 않는 한국 스타벅스 음료 데이터 추가
            - 예시: "제주 말차 라떼" -> 미국에는 없는 음료
    - 🔹 컬럼 분리 및 간소화: 
        - 여러 데이터가 결합된 컬럼을 분리하여 가독성 향상 및 분석 용이성 증대
             - 예시: 음료의 사이즈와 유제품 여부 데이터가 들어있는 "Beverage_prep" 컬럼을 "사이즈", "유제품"으로 분리
    """)

    st.markdown("---")
    
    st.markdown('<h2>💿 데이터베이스 생성</h2>', unsafe_allow_html=True)
    
    st.markdown('<h4>📌 데이터베이스 유형</h4>', unsafe_allow_html=True)
    st.write("""
    - **user_data.csv** : 
        - 목적 : 사용자 정보 저장
        - 컬럼 : 사용자 ID, 이름, 비밀번호 등
    """)
    
    st.info('🔍 **데이터 샘플**')
    df_user = pd.read_csv('data/user_data.csv')
    st.dataframe(df_user.head(1))

    st.write("""
    - **order_data.csv** :
        - 목적 : 주문 내역 저장
        - 컬럼 : 사용자 ID, 음료명, 주문 수 등
    """)

    st.info('🔍 **데이터 샘플**')
    df_log = pd.read_csv('data/order_data.csv')
    st.dataframe(df_log.head(1))

    st.write("""
    - **review_data.csv** :
        - 목적 : 리뷰 정보 저장
        - 컬럼 : 사용자 ID, 음료명, 평점, 리뷰 텍스트 등
    """)

    st.info('🔍 **데이터 샘플**')
    df_review = pd.read_csv('data/review_data.csv')
    st.dataframe(df_review.head(1))


    st.markdown("---")
    

    st.markdown('<h2>🎭 회원가입 및 로그인 시스템 구축</h2>', unsafe_allow_html=True)

    st.markdown('<h4>📌 필요성</h4>', unsafe_allow_html=True)
    st.write('- 개인별 취향에 맞는 음료의 추천 위해 로그인이 필요')

    st.markdown('<h4>📌 사용한 기법</h4>', unsafe_allow_html=True)
    st.write("""
    - 데이터베이스 연동: 사용자 정보를 데이터베이스에 저장하고 관리
        - 회원가입 시 사용자 정보를 데이터베이스에 저장
        - 로그인 시 입력된 정보를 데이터베이스와 비교하여 인증
    - 세션 관리: 사용자의 로그인 상태를 유지하기 위해 세션을 관리
        - 앱 실행 시 최초 세션을 로그아웃 상태로 설정
        - 로그인 시 세션을 로그인 상태로 변경
        - 이후 세션 유지를 통해 탭 변경에도 로그인 상태 유지
    """)

    st.markdown('<h4>📌 회원가입 및 로그인 프로세스</h4>', unsafe_allow_html=True)
    st.write("""
    - 회원가입: 사용자 정보를 입력받아 데이터베이스에 저장
        - ID 중복 여부 확인 후 회원가입 허용
        - 사용자 이름, ID, 비밀번호 저장
    - 로그인: 입력된 사용자 정보를 데이터베이스와 비교하여 인증
        - 사용자 ID 및 비밀번호의 조합이 일치하는지 확인 후 로그인 허용
        - 로그인 성공 시 사용자 이름을 화면에 출력
    """)

    st.markdown('<h4>📌 사용자 입력 예시</h5>', unsafe_allow_html=True)
    st.markdown("""
                ```bash
                ID: abc
                PW: alpha
                ```""")

    st.markdown('<h4>📌 출력 결과</h4>', unsafe_allow_html=True)
    st.markdown("""
                ```bash
                ▶ 홍길동님, 환영합니다! 🎉
                """)

    st.markdown("<h4>📌 활용 방안</h4>", unsafe_allow_html=True)
    st.write("""
    - ID로 사용자별 음료 주문 및 리뷰 작성 기록 구분: 개인 맞춤형 음료 추천에 활용
        - 회원가입이 없을 경우 주문 및 리뷰 작성 불가능
    - 주문 내역 및 리뷰 관리
        - 사용자의 음료 주문 빈도 및 리뷰 작성/수정 가능
    """)


    st.markdown("---")
    

    st.markdown('<h2>🎟 주문 시스템 구축</h2>', unsafe_allow_html=True)

    st.markdown('<h4>📌 필요성</h4>', unsafe_allow_html=True)
    st.write('- 사용자가 실제로 구매한 음료가 무엇인지 파악하고 이를 기반으로 이후 추천에 반영')

    st.markdown('<h4>📌 주문 정보 저장 프로세스</h4>', unsafe_allow_html=True)
    st.write("""
    - 데이터베이스 연동: 주문 정보를 데이터베이스에 저장
        - 사용자 ID, 음료명, 사이즈 등의 정보 저장
            - 사용자가 처음 주문한 음료: 새로운 행으로 저장
            - 사용자가 이미 주문한 음료: 해당 행의 '주문 수' 컬럼의 값 1 증가
    - 사용자 인터페이스: 사용자가 쉽게 주문할 수 있도록 직관적인 UI 제공
        - 음료 유형, 음료 선택, 사이즈 선택 등의 정보 입력만으로 주문이 가능하도록 구성
    """)

    st.markdown('<h4>📌 사용자 입력 예시</h4>', unsafe_allow_html=True)
    st.markdown("""
                ```bash
                음료 유형 선택 : 에스프레소
                음료 선택 : 아이스 카페 아메리카노
                사이즈 선택 : Tall
                """)

    st.markdown('<h4>📌 출력 결과</h4>', unsafe_allow_html=True)
    st.markdown("""
                ```bash
                ▶ 아이스 카페 아메리카노 주문이 완료되었습니다! ☕️
                """)

    st.markdown('<h4>📌 활용 방안</h4>', unsafe_allow_html=True)
    st.write("""
    - 주문 데이터를 기반으로 사용자 맞춤형 추천 제공
        - 사용자의 주문 이력을 기반으로 사용자가 자주 마시는 음료 파악
    - 주문 내역을 통해 인기 음료 분석
        - 사용자 개개인의 주문 이력을 수집하여 소비자 전반의 선호도 파악
    """)

    st.markdown("---")
    

    st.markdown('<h2>🌍 음료 추천 서비스</h2>', unsafe_allow_html=True)

    st.markdown('<h4>📌 목표</h4>', unsafe_allow_html=True)
    st.write('- 사용자들의 주문 이력을 바탕으로 각 사용자에게 맞는 음료 추천')

    st.markdown('<h4>📌 사용 기법</h4>', unsafe_allow_html=True)
    st.write("""
    - 데이터베이스 연동: 사용자의 주문 데이터를 데이터베이스에서 불러와 분석
        - 사용자 본인의 음료 주문 이력을 기반으로 추천
    - 콘텐츠 기반 필터링: 요청의 속성을 분석하여 유사한 속성의 음료 추천
    - 협업 필터링: 사용자의 요청을 기반으로 다른 사용자의 주문 및 리뷰 이력을 활용하여 음료 추천
    """)

    st.markdown('<h4>📌 추천 옵션 및 프로세스</h4>', unsafe_allow_html=True)
    st.write("""
    - 1. **늘 먹던 걸로.**
        - 사용자의 과거 주문 내역을 기반으로 추천
            - 사용자가 자주 주문한 음료 중 요청한 세부 옵션에 부합하는 음료 추천
        - 첫 주문이거나 요청한 세부 옵션에 부합하는 음료가 없는 경우 다시 선택하도록 유도
    - 2. **피곤해요.. 혈중 카페인 농도 부족!**
        - 카페인 함량이 높은 음료 추천
            - 사용자의 과거 주문 내역 기반, 카페인 함량이 전체 평균 이상인 음료 추천
        - 사용자의 과거 주문 음료 중 카페인 함량이 전체 평균 이상인 음료가 없을 경우
            - 전체 음료 리스트 중 카페인 함량이 높은 음료 추천
    - 3. **그냥 아주 달달한 거 주세요.**
        - 당 함량이 높은 음료 추천
            - 사용자의 과거 주문 내역 기반, 당 함량이 전체 평균 이상인 음료 추천
        - 사용자의 과거 주문 음료 중 당 함량이 전체 평균 이상인 음료가 없을 경우
            - 전체 음료 리스트 중 당 함량이 높은 음료 추천
    - 4. **죄책감은 최소로! 맛은 그대로!**
        - 저칼로리 음료 추천
            - 사용자의 과거 주문 내역 기반, 칼로리가 전체 평균 이하인 음료 추천
        - 사용자의 과거 주문 음료 중 칼로리가 전체 평균 이하인 음료가 없을 경우
            - 전체 음료 리스트 중 칼로리가 낮은 음료 추천
    - 5. **오늘은 새로운 게 궁금해!**
        - 새로운 음료 추천
             - 사용자가 주문한 이력이 없는 음료 중 추천 점수가 0 이상인 음료 목록 추출
                - 추천 점수: 사용자들의 리뷰 데이터 및 별점을 기반으로 산출
            - 해당 음료 중 랜덤으로 추천 (**.sample()** 사용)
    """)

    st.markdown('<h4>📌 사용자 입력 예시</h5>', unsafe_allow_html=True)
    st.markdown("""
                ```bash
                옵션 : 그냥 아주 달달한 거 주세요.
                유제품 : 우유 든 걸로!
                사이즈 : Tall
                """)

    st.markdown('<h4>📌 출력 결과</h4>', unsafe_allow_html=True)
    st.markdown("""
                ```bash
                ▶ 달달한 거 너무 좋죠,
                Tall 사이즈 딸기 아사이 레모네이드 스타벅스 리프레셔
                어때요?
                """)
    
    st.markdown('<h4>📌 추천 결과 기반 주문 시스템</h4>', unsafe_allow_html=True)
    st.write("""
    - '이거 마실래요' 버튼 클릭 시 주문이 이루어짐
    - 상술한 주문 시스템과 동일한 방식으로 주문 완료
        - 주문 정보를 데이터베이스에 저장
    """)

    st.markdown('<h4>📌 출력 결과</h4>', unsafe_allow_html=True)
    st.markdown("""
                ```bash
                ▶ 제 추천이 마음에 드시길 바래요!
                """)

    st.markdown('<h4>📌 활용 방안</h4>', unsafe_allow_html=True)
    st.write("""
    - 사용자 맞춤형 음료 추천을 통해 만족도 향상
        - 사용자 취향에 맞는 음료 추천으로 긍정적 리뷰 증가 및 평점 향상
    - 추천 시스템을 통해 새로운 음료 홍보
        - 사용자가 주문한 이력이 없는 음료를 추천하여 새로운 음료 홍보
    """)


    st.markdown("---")
    

    st.markdown('<h2>🌍 리뷰 작성 시스템</h2>', unsafe_allow_html=True)

    st.markdown('<h4>📌 목표</h4>', unsafe_allow_html=True)
    st.write('- 음료에 대한 사용자들의 의견 수집 및 이를 바탕으로 추천 시스템 개선')

    st.markdown('<h4>📌 사용 기법</h4>', unsafe_allow_html=True)
    st.write("""
        - 자연어 처리 모델: 리뷰 텍스트를 분석하여 긍정/부정 여부 분석
            - Hugging Face의 AI모델 활용
                - 모델명 : distilbert/distilbert-base-uncased-finetuned-sst-2-english
        - 번역 모델: 한글 리뷰를 영문으로 번역하여 분석
            - 상술한 자연어 처리 모델이 영문 텍스트를 기반으로 학습되어 있기 때문
            - Hugging Face의 AI모델 활용
                - 모델명 : yeeunlee/opus-mt-ko-en-finetuned
        - 데이터베이스 연동: 리뷰 정보를 데이터베이스에 저장
            - review_data.csv에 사용자 ID, 음료명, 평점, 리뷰 텍스트 등의 정보 저장
            - 사용자가 입력한 별점에 리뷰 텍스트의 긍정/부정 여부에 따른 가중치를 곱하여 추천 점수로 menu_data.csv에 저장
    """)

    st.markdown('<h4>📌 리뷰 작성/수정 및 저장 프로세스</h4>', unsafe_allow_html=True)
    st.write("""
    - 사용자가 음료에 대한 리뷰를 작성하고 제출
        - 사용자가 실제로 구입한 음료인지 여부 확인
        - 해당 음료에 대해 리뷰를 작성한 이력이 없을 경우
             - 새로운 행으로 리뷰 정보 저장
        - 해당 음료에 대해 리뷰를 작성한 이력이 있을 경우
             - 기존 리뷰 정보 수정
    - 제출된 리뷰를 데이터베이스에 저장
        - review_data.csv에 사용자 ID, 음료명, 평점, 리뷰 텍스트 등의 정보 저장
    - 리뷰 텍스트와 별점 기반으로 추천 점수 계산
        - 사용자의 리뷰 텍스트를 번역하여 영문 텍스트로 변환
        - 변환된 텍스트를 자연어 처리 모델에 입력하여 긍정/부정 여부 분석
        - 분석 결과를 바탕으로 추천 점수 계산
            - 추천 점수를 기반으로 메뉴 데이터의 '추천 점수' 항목 업데이트
    """)

    st.markdown('<h4>📌 사용자 입력 예시</h5>', unsafe_allow_html=True)
    st.markdown("""
                ```bash
                음료 유형 : 에스프레소
                음료 : 아이스 카페 아메리카노
                사이즈 : Tall
                별점 : 4
                리뷰 : 맛있어요!
                """)

    st.markdown('<h4>📌 출력 결과</h4>', unsafe_allow_html=True)
    st.markdown("""
                ```bash
                ▶ 리뷰가 성공적으로 제출되었습니다! 감사합니다. 🎉
                """)
    
    st.markdown('<h4>📌 활용 방안</h4>', unsafe_allow_html=True)
    st.write("""
    - 리뷰 데이터를 분석하여 음료의 장단점 파악
        - 사용자들의 의견을 바탕으로 음료의 맛, 가격, 서비스 등을 분석하고 개선
    - 리뷰를 바탕으로 음료 추천 시스템 개선
        - 사용자들의 리뷰를 바탕으로 추천 점수를 계산하여 추천 시스템 정교화
    """)


    st.markdown("---")
    

    st.markdown('<h2>🎯 향후 개선 가능성</h2>', unsafe_allow_html=True)
    st.write("""
    - 음성 인식 기능 추가: 음성으로 음료 주문 및 리뷰 작성 가능
    - 실시간 추천 시스템: 사용자의 현재 상태(예: 날씨, 기분)에 따라 실시간으로 음료 추천
    - 주문 시스템 실제화: 실제 스타벅스 앱과 연동하여 주문 가능하도록 확장
    """)

    st.markdown("---")