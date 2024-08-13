import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# 加载环境变量
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# 初始化 Gemini 模型
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

# 定义提示模板
prompt_template = PromptTemplate.from_template("Write a tweet about {topic}.")

# 创建 LLM 链
llm_chain = LLMChain(llm=llm, prompt=prompt_template, verbose=True)

# Streamlit 用户界面
st.title("Gemini with LangChain on Streamlit")
topic = st.text_input("Enter a topic:", "")

if st.button("Generate"):
    if topic:
        response = llm_chain.run(topic=topic)
        st.write(response)
    else:
        st.warning("Please enter a topic!")
