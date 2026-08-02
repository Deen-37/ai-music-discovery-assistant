from src.agent import MusicAgent
from src.llm import LLMClient
agent = MusicAgent()

result = agent.recommend(
    "I need relaxing music while studying."
)

print(result)