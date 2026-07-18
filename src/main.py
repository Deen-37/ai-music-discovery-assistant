"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from src.recommender import load_songs, recommend_songs
except ModuleNotFoundError:
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print_recommendations(user_prefs, recommendations)


def print_recommendations(user_prefs: dict, recommendations: list) -> None:
    """Render recommendations as a clean, readable terminal report."""
    WIDTH = 60

    # Header
    print()
    print("=" * WIDTH)
    print("  TOP SONG RECOMMENDATIONS".center(WIDTH))
    print("=" * WIDTH)
    print(
        f"  Profile: {user_prefs['favorite_genre']} / "
        f"{user_prefs['favorite_mood']} / "
        f"energy {user_prefs['target_energy']}"
    )
    print("=" * WIDTH)

    if not recommendations:
        print("\n  No recommendations found.\n")
        return

    for rank, rec in enumerate(recommendations, start=1):
        song = rec["song"]
        score = rec["score"]
        reasons = rec["reasons"]

        title = song["title"]
        artist = song.get("artist", "Unknown Artist")

        print()
        print(f"  #{rank}  {title}")
        print(f"      by {artist}")
        print(f"      Score: {score:.2f}")
        print("      Reasons:")
        for reason in reasons:
            print(f"        - {reason}")

    print()
    print("=" * WIDTH)
    print()


if __name__ == "__main__":
    main()
