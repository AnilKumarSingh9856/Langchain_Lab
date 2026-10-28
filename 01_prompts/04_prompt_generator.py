from pathlib import Path

from langchain_core.prompts import PromptTemplate

TEMPLATE_PATH = Path(__file__).with_name("04a_template.json")

template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}".

Explanation style: {style_input}
Explanation length: {length_input}
Additional focus or question: {user_input}

1. Include relevant mathematical equations from the paper and explain them simply.
2. Use relatable analogies to clarify complex ideas.
3. Include intuitive code snippets where applicable.
4. If information is unavailable, say: "Insufficient information available."

Ensure the summary is clear, accurate, and aligned with the requested style and length.
""",
    input_variables=["paper_input", "style_input", "length_input", "user_input"],
    validate_template=True,
)

if __name__ == "__main__":
    template.save(str(TEMPLATE_PATH))
