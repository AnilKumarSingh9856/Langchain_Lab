import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


model = ChatOpenAI(
    model="openai/gpt-4o-mini",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    max_tokens=512,
)

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == "exist":
        break

    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print(f"AI: {result.content}")


for chat in chat_history:
    print(chat)
