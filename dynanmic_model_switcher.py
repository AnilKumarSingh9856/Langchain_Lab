import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

if not OPENROUTER_API_KEY:
    raise RuntimeError("Set OPENROUTER_API_KEY in your .env file or environment.")

# 2. Define our budget-friendly learning models
BUDGET_MODELS = {
    "openai": "openai/gpt-4o-mini",
    "google": "google/gemini-2.5-flash",
    "anthropic": "anthropic/claude-3-haiku",
}


def get_chat_model(provider: str, temperature: float = 0.7):
    """Helper function to switch models efficiently"""
    if provider not in BUDGET_MODELS:
        raise ValueError(f"Provider must be one of: {list(BUDGET_MODELS.keys())}")

    return ChatOpenAI(
        model=BUDGET_MODELS[provider],
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL,
        temperature=temperature,
        max_tokens=1024,
    )


# ==========================================
# 🚀 LEARNING EXERCISE: Running the Models
# ==========================================

# Create a basic prompt template
prompt = ChatPromptTemplate.from_template(
    "Explain the concept of {topic} to a 10-year-old."
)

# Change this string to "google", "anthropic", or "openai" to switch instantly!
CURRENT_PROVIDER = "google"

# Initialize the selected budget model
llm = get_chat_model(CURRENT_PROVIDER)

# Chain them together using LangChain Expression Language (LCEL)
chain = prompt | llm

# Execute the run
print(f"--- Sending request to {BUDGET_MODELS[CURRENT_PROVIDER]} ---")
response = chain.invoke({"topic": "API keys"})
print(response.content)
