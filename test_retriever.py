from src.retriever import MusicRetriever

retriever = MusicRetriever()

tests = [
    "I need relaxing music while studying.",
    "Play energetic music for the gym.",
    "I want happy pop songs.",
    "I feel sad today.",
    "Play some jazz while drinking coffee."
]

for test in tests:
    print(f"\nUser: {test}")
    print("-" * 50)

    songs = retriever.retrieve(test)
    print(f"Retrieved {len(songs)} songs")

    for song in songs:
        print(song["title"], "-", song["artist"])
    for song in songs:
        print(f"{song['title']} | {song['genre']} | {song['mood']}")