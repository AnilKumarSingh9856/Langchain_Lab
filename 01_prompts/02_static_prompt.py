import os

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model="openai/gpt-4o-mini",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    max_tokens=512,
)

st.header("Research Paper Summarizer")

user_input = st.text_input("Enter your query")

if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)

# command to run `streamlit run 02_static_prompt.py` i.e. a file name and open file inside the integrated terminal by right click and choose option of intergrated terminal
