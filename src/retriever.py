import pandas as pd


class MusicRetriever:
    """
    Retrieves songs from the dataset based on the user's preferences.
    This is the Retrieval part of the RAG system.
    """

    def __init__(self, csv_path: str):
        """
        Loads the music dataset into memory.

        Args:
            csv_path (str): Path to the songs.csv file.
        """

        # Read the CSV file into a Pandas DataFrame.
        self.songs = pd.read_csv(csv_path)

    def retrieve(self, preferences: dict, top_k: int = 5):
        """
        Finds songs matching the user's preferences.

        Args:
            preferences (dict): User preferences such as genre or mood.
            top_k (int): Maximum number of songs to return.

        Returns:
            DataFrame: Top matching songs.
        """

        # Start with the complete dataset.
        results = self.songs.copy()

        # Filter by genre if the user specified one.
        if "genre" in preferences:
            results = results[
                results["genre"].str.lower()
                == preferences["genre"].lower()
            ]

        # Filter by mood if the user specified one.
        if "mood" in preferences:
            results = results[
                results["mood"].str.lower()
                == preferences["mood"].lower()
            ]

        # Return only the requested number of songs.
        return results.head(top_k)