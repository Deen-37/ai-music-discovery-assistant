from src.llm import LLMClient

# Create an instance of our LLM client.
llm = LLMClient()

# Ask the model a simple question.
response = llm.generate(
    "Recommend relaxing music for studying."
)

print(response)