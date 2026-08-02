"""
Stores all prompts used by the AI Music Discovery Assistant.
Keeping prompts here makes the project easier to maintain.
"""


def recommendation_prompt(user_request: str, song_list: str) -> str:
    """
    Build the prompt sent to the LLM.
    """

    return f"""
You are an AI Music Discovery Assistant.

User Request:
{user_request}

Retrieved Songs:
{song_list}

Recommend the best 3 songs.

Rules:
- ONLY use the retrieved songs.
- Do NOT invent songs.
- Explain briefly why each song matches.

Return ONLY valid JSON.

[
    {{
        "title": "...",
        "artist": "...",
        "reason": "..."
    }}
]
"""