import sqlite3

# Maps common user terms to keywords that exist in our dataset.
QUERY_MAP = {
    "study": ["focused", "lofi", "chill"],
    "studying": ["focused", "lofi", "chill"],
    "coding": ["focused", "lofi"],
    "workout": ["intense", "pop", "edm"],
    "gym": ["intense", "pop", "edm"],
    "sleep": ["ambient", "relaxed", "classical"],
    "relax": ["relaxed", "chill", "ambient"],
    "relaxing": ["relaxed", "chill", "ambient"],
    "party": ["party", "latin", "edm"],
    "happy": ["happy", "pop"],
}


class MusicRetriever:
    """
    Retrieves the most relevant songs from the SQLite database.
    """

    def __init__(self, db_path="music.db"):
        """
        Initialize the retriever.

        Args:
            db_path (str): Path to the SQLite database.
        """
        self.db_path = db_path

    def retrieve(self, user_request: str, top_k: int = 5):
        """
        Retrieve the top matching songs using weighted scoring.

        Args:
            user_request (str): Natural language request from the user.
            top_k (int): Number of songs to return.

        Returns:
            list: List of matching SQLite Row objects.
        """

        # Connect to the SQLite database.
        connection = sqlite3.connect(self.db_path)

        # Allow rows to behave like dictionaries.
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()

        # Retrieve every song from the database.
        cursor.execute("SELECT * FROM songs")
        songs = cursor.fetchall()

        connection.close()

        # Convert the user's request to lowercase.
        query = user_request.lower()

        # Expand the query using related keywords.
        expanded_query = query

        for word, keywords in QUERY_MAP.items():
            if word in query:
                expanded_query += " " + " ".join(keywords)

        # Store each song along with its score.
        scored_songs = []

        for song in songs:

            score = 0

            # Genre matches are highly important.
            if song["genre"].lower() in expanded_query:
                score += 3

            # Mood matches are highly important.
            if song["mood"].lower() in expanded_query:
                score += 3

            # Artist matches are moderately important.
            if song["artist"].lower() in expanded_query:
                score += 2

            # Title matches are moderately important.
            if song["title"].lower() in expanded_query:
                score += 2

            # Save the score with the song.
            # Keep only songs that matched at least one keyword.
            if score > 0:
                scored_songs.append((score, song))

        # Sort songs by score (highest first).
        scored_songs.sort(
            key=lambda item: item[0],
            reverse=True
        )

        # Return only the top-k songs.
        return [
            song
            for score, song in scored_songs[:top_k]
        ]