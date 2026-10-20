import os

import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model="openai/gpt-4o-mini",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    max_tokens=512,
)

template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}".

Explanation style: {style_input}
Explanation length: {length_input}

1. Include relevant mathematical equations from the paper and explain them simply.
2. Use relatable analogies to clarify complex ideas.
3. Include intuitive code snippets where applicable.
4. If information is unavailable, say: "Insufficient information available."

Ensure the summary is clear, accurate, and aligned with the requested style and length.
""",
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True, # if any of those above field missing it generate error
)

## Why use PromptTemplate over f-strings
"""
    1. Default validation
    2. Resuable
    3. Langchain Ecosystem
"""

st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis",
    ],
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"],
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)",
    ],
)

# user_input = st.text_input("Enter an additional focus or question")

if st.button("Summarize"):
    prompt = template.invoke(
        {
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input,
        }
    )
    result = model.invoke(prompt)
    st.write(result.content)
