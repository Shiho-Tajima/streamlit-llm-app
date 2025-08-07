from dotenv import load_dotenv  # .envファイルから環境変数を読み込む
import streamlit as st  # Streamlitのインポート（Webアプリ作成用）
from langchain.llms import OpenAI  # LangChainのOpenAI LLMクラスをインポート

load_dotenv()  # .envファイルの環境変数を読み込む

# アプリのタイトルを表示
st.title("LLM Demo with LangChain")

# アプリの説明文を表示
st.write("""
このアプリは、LangChainとOpenAIを利用した大規模言語モデル（LLM）デモです。
質問を入力し、「送信」ボタンを押すと、AIが回答します。
また、専門家の種類（心理またはIT）を選択することで、異なる視点からの回答も得られます。
""")

# ユーザーからの質問入力欄
user_input = st.text_input("質問を入力してください:")

# 専門家の種類を選択するラジオボタン
expert_type = st.radio("専門家の種類を選択してください:", ("心理", "IT"))

# 送信ボタンが押され、かつ質問が入力されている場合の処理
if st.button("送信") and user_input:
    # 専門家の種類に応じてLLMの応答を生成する関数
    def get_llm_response(user_input: str, expert_type: str) -> str:
        if expert_type == "心理":
            system_message = "あなたは心理の領域の専門家です。"
        elif expert_type == "IT":
            system_message = "あなたはITの領域の専門家です。"
        else:
            system_message = ""
        llm = OpenAI(temperature=0)
        prompt = f"{system_message} {user_input}"
        return llm(prompt)

    response = get_llm_response(user_input, expert_type)
    st.write("回答:")
    st.write(response)
