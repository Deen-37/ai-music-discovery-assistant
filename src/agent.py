import json

from src.llm import LLMClient
from src.retriever import MusicRetriever
from src.guardrails import Guardrails
from src.prompts import recommendation_prompt

class MusicAgent:
    """
    Coordinates the complete RAG workflow.
    """

    def __init__(self, db_path="music.db"):
        # Initialize each component.
        self.retriever = MusicRetriever(db_path)
        self.llm = LLMClient()
        self.guardrails = Guardrails()

    def recommend(self, user_request: str):
        """
        Generate AI music recommendations.

        Args:
            user_request (str): User's natural language request.

        Returns:
            list | dict | str
        """

        # Retrieve the most relevant songs.
        songs = self.retriever.retrieve(user_request)

        if not songs:
            return "Sorry, I couldn't find any matching songs."

        # Save the valid song titles.
        valid_titles = [song["title"] for song in songs]

        # Build a readable list for the LLM.
        song_list = ""

        for song in songs:
            song_list += (
                f"Title: {song['title']}\n"
                f"Artist: {song['artist']}\n"
                f"Genre: {song['genre']}\n"
                f"Mood: {song['mood']}\n\n"
            )

        # Prompt the LLM.
        prompt = recommendation_prompt(
            user_request,
            song_list
        )

        # Ask the LLM.
        response = self.llm.generate(prompt)

        # Convert JSON into Python.
        recommendations = json.loads(response)

        # Validate recommendations.
        valid, invalid_titles = self.guardrails.validate(
            recommendations,
            valid_titles
        )

        if not valid:
            return {
                "error": "Guardrail validation failed.",
                "invalid_titles": invalid_titles
            }

        return recommendations

