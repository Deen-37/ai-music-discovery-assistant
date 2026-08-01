from src.agent import MusicAgent

# Create the AI agent.
agent = MusicAgent("data/songs.csv")

# Example preferences.
preferences = {
    "genre": "lofi",
    "mood": "focused"
}

# Generate recommendations.
response = agent.recommend(preferences)

print(response)