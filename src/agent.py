from src.llm import LLMClient
from src.retriever import MusicRetriever


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

        # If no songs match, stop early.
        if songs.empty:
            return "Sorry, I couldn't find any matching songs."

        # Convert the retrieved songs into text so the LLM can read them.
        song_list = songs.to_string(index=False)

        # Build the prompt that will be sent to the model.
        prompt = f"""
You are an AI Music Discovery Assistant.

Use ONLY the songs below.

{song_list}

Recommend the best songs for the user.

Explain why each song matches in one short sentence.

Do not invent songs.
"""

        # Ask the LLM to generate the recommendation.
        return self.llm.generate(prompt)