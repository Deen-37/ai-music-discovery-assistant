from src.llm import LLMClient

llm = LLMClient()

prompt = """
You are an AI Music Discovery Assistant.

User Request:
I need relaxing music while studying.

Retrieved Songs:

1. Focus Flow | LoRoom | lofi | focused
2. Library Rain | Paper Lanterns | lofi | chill
3. Spacewalk Thoughts | Orbit Bloom | ambient | chill

Recommend the best 2 songs.

Return ONLY JSON.

[
  {
    "title": "...",
    "artist": "...",
    "reason": "..."
  }
]

Do NOT recommend songs outside the retrieved list.
"""

print(llm.generate(prompt))