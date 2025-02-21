import streamlit as st
import os
from huggingface_hub import InferenceClient


def get_huggingface_token():
    token = os.environ.get('HUGGINGFACE_API_TOKEN')
    if token is None:
        token = st.secrets.get('HUGGINGFACE_API_TOKEN')
    return token

# QnA 챗봇 UI
st.title("💬 WorkBot")
st.write("노동 분야 관련 질문을 입력하면 AI가 답변해드립니다.")

# AI 응답 처리 함수
def get_response(chat):
    st.markdown("---")
    with st.spinner("WorkBot이 답변을 생성 중입니다..."):  # AI 응답 생성 중 스피너 표시
        prompt = """
        당신은 노동법 및 근로기준법 전문가입니다.
        노동 및 근로 관련 질문만 아주 정확하게, 그리고 구체적으로 답변해 주세요.
        늘 존댓말로 대답해야 합니다.
        그리고 근거를 꼭 명시해주세요. 근거가 미비한 경우에는 확인이 필요한 정보라고 언급해주세요.
        수치에 대해 물어볼 경우 정확한 데이터를 제공하세요.
        링크 제공 시 해당 링크가 유효한지 확인하세요.
        혹시라도 답변이 부정확하다고 생각되는 경우에는 그 이유를 꼭 설명해주세요.
        노동 및 근로 관련 질문이 아닐 경우 정중하게 답변을 거절해주세요.
        의견을 제공해야 할 경우 아주 정중하게 답변을 거절해주세요.
        이상의 지침을 준수하여 꼼꼼하게 답변해 주시기 바랍니다.

        
        질문: {}
        답변:""".format(chat)

        response = client.text_generation(prompt, max_new_tokens=1024)

        cleaned_text = "\n".join(line.lstrip() for line in response.splitlines()
                                    if line.strip())


        st.markdown(f"**질문**: {chat}")  # 질문 출력
        st.text("")
        st.markdown(f"**답변**: {cleaned_text}")  # 답변 출력
        st.markdown("---")

token = get_huggingface_token()
api_key = os.getenv(token)
client = InferenceClient(model="google/gemma-2-9b-it", token=api_key)

chat = st.chat_input("질문을 입력하세요:")

if chat:
    get_response(chat)