from src.agent import MusicAgent


def print_recommendations(recommendations):
    """Display recommendations in a presentation-friendly format."""
    if isinstance(recommendations, str):
        print(f"\n{recommendations}")
        return

    if isinstance(recommendations, dict) and "error" in recommendations:
        print(f"\nError: {recommendations['error']}")
        return

    print("\n" + "=" * 58)
    print("           YOUR MUSIC RECOMMENDATIONS")
    print("=" * 58)

    for number, song in enumerate(recommendations, start=1):
        print(f"\n{number}. {song['title']} — {song['artist']}")
        print(f"   Why: {song['reason']}")

    print("\n" + "=" * 58)


agent = MusicAgent()
request = input("What kind of music would you like? ")
result = agent.recommend(request)
print_recommendations(result)
