from src.llm import LLMClient
from src.retriever import MusicRetriever
import json
from src.guardrails import Guardrails

class MusicAgent:
    """
    Coordinates the workflow of our AI Music Discovery Assistant.
    """

    def __init__(self, csv_path: str):
        # Initialize the retriever (RAG component).
        self.retriever = MusicRetriever(csv_path)

        # Initialize the local LLM.
        self.llm = LLMClient()

    def recommend(self, preferences: dict) -> str:
        """
        Retrieves relevant songs and asks the LLM
        to generate personalized recommendations.

        Args:
            preferences (dict): User preferences.

        Returns:
            str: AI-generated recommendation.
        """

        # Retrieve songs matching the user's preferences.
        songs = self.retriever.retrieve(preferences)

        # Create a list of valid song titles for validation.
        valid_titles = songs["title"].tolist()
        # If no songs match, stop early.
        if songs.empty:
            return "Sorry, I couldn't find any matching songs."

        # Convert the retrieved songs into text so the LLM can read them.
        song_list = songs.to_string(index=False)

        # Build the prompt that will be sent to the model.
        # Build the prompt that will be sent to the LLM.
        prompt = f"""
You are an AI Music Discovery Assistant.

Use ONLY the songs listed below.

Do NOT invent songs.
Do NOT recommend songs outside this list.

Return ONLY valid JSON.

The JSON format must be:

[
    {{
        "title": "...",
        "artist": "...",
        "reason": "..."
    }}
]

Retrieved Songs:

{song_list}
"""

        

        # Generate a response from the LLM.
        response = self.llm.generate(prompt)

        # Convert the JSON string into Python objects.
       

    # Convert the JSON response into a Python list.
        recommendations = json.loads(response)



        guardrails = Guardrails()

        is_valid, invalid_titles = guardrails.validate(
            recommendations,
            valid_titles
        )

        if not is_valid:
            return {
                "error": "Guardrail validation failed.",
                "invalid_titles": invalid_titles
            }

        return recommendations