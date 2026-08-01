from src.retriever import MusicRetriever

# Create the retriever.
retriever = MusicRetriever("data/songs.csv")

# Example user preferences.
preferences = {
    "genre": "lofi",
    "mood": "focused"
}

# Retrieve matching songs.
songs = retriever.retrieve(preferences)

print(songs)