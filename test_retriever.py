import sqlite3
from pathlib import Path

import pytest

from src.retriever import MusicRetriever

# A small, fixed catalog so results don't depend on music.db.
SONGS = [
    (1, "Library Rain", "Paper Lanterns", "lofi", "chill"),
    (2, "Midnight Coding", "LoRoom", "lofi", "focused"),
    (3, "Gym Hero", "Max Pulse", "pop", "intense"),
    (4, "Sunrise City", "Neon Echo", "pop", "happy"),
    (5, "Desert Mirage", "Sand Pulse", "edm", "party"),
    (6, "Coffee Shop Stories", "Slow Stereo", "jazz", "relaxed"),
    (7, "Storm Runner", "Voltline", "rock", "intense"),
    (8, "Spacewalk Thoughts", "Orbit Bloom", "ambient", "chill"),
]


@pytest.fixture
def retriever(tmp_path):
    """Build a temporary database with the same schema as database.py."""
    db_path = tmp_path / "test_music.db"

    connection = sqlite3.connect(db_path)
    connection.execute("""
        CREATE TABLE songs (
            id INTEGER PRIMARY KEY,
            title TEXT,
            artist TEXT,
            genre TEXT,
            mood TEXT,
            energy REAL,
            tempo_bpm INTEGER,
            valence REAL,
            danceability REAL,
            acousticness REAL
        )
    """)
    connection.executemany(
        "INSERT INTO songs VALUES (?, ?, ?, ?, ?, 0.5, 100, 0.5, 0.5, 0.5)",
        SONGS
    )
    connection.commit()
    connection.close()

    return MusicRetriever(str(db_path))


def titles(songs):
    return [song["title"] for song in songs]


# ---------- Matching ----------

def test_genre_match(retriever):
    assert titles(retriever.retrieve("Play some jazz")) == ["Coffee Shop Stories"]


def test_mood_match(retriever):
    result = titles(retriever.retrieve("something intense"))
    assert sorted(result) == ["Gym Hero", "Storm Runner"]


def test_artist_match(retriever):
    assert titles(retriever.retrieve("anything by Voltline")) == ["Storm Runner"]


def test_title_match(retriever):
    assert titles(retriever.retrieve("play library rain")) == ["Library Rain"]


def test_matching_is_case_insensitive(retriever):
    assert titles(retriever.retrieve("JAZZ")) == ["Coffee Shop Stories"]


def test_no_match_returns_empty_list(retriever):
    assert retriever.retrieve("polka accordion") == []


def test_empty_request_returns_empty_list(retriever):
    assert retriever.retrieve("") == []


# ---------- Query expansion ----------

def test_study_expands_to_lofi_focused_chill(retriever):
    result = titles(retriever.retrieve("music for studying"))

    # Both lofi songs score 6 (genre + mood), Spacewalk only 3 (mood).
    assert sorted(result[:2]) == ["Library Rain", "Midnight Coding"]
    assert result[2:] == ["Spacewalk Thoughts"]


def test_gym_expands_to_intense_pop_edm(retriever):
    result = titles(retriever.retrieve("music for the gym"))

    # Gym Hero matches both pop and intense, so it ranks first.
    assert result[0] == "Gym Hero"
    assert sorted(result[1:]) == ["Desert Mirage", "Storm Runner", "Sunrise City"]


def test_sleep_expands_to_ambient(retriever):
    result = titles(retriever.retrieve("help me sleep"))
    assert sorted(result) == ["Coffee Shop Stories", "Spacewalk Thoughts"]


# ---------- Ranking ----------

def test_genre_outranks_title(retriever):
    # Genre match is worth 3, title match only 2.
    result = titles(retriever.retrieve("library rain or jazz"))
    assert result == ["Coffee Shop Stories", "Library Rain"]


def test_genre_and_mood_outrank_single_match(retriever):
    result = titles(retriever.retrieve("happy pop"))
    assert result[0] == "Sunrise City"
    assert result[1:] == ["Gym Hero"]


# ---------- Result size and shape ----------

def test_default_returns_at_most_five(retriever):
    # This request matches six songs.
    result = retriever.retrieve("chill intense pop lofi")
    assert len(result) == 5


def test_top_k_limits_results(retriever):
    assert len(retriever.retrieve("music for the gym", top_k=2)) == 2


def test_results_expose_song_fields(retriever):
    song = retriever.retrieve("Play some jazz")[0]

    assert song["artist"] == "Slow Stereo"
    assert song["genre"] == "jazz"
    assert song["mood"] == "relaxed"


def test_missing_songs_table_raises(tmp_path):
    retriever = MusicRetriever(str(tmp_path / "empty.db"))

    with pytest.raises(sqlite3.OperationalError):
        retriever.retrieve("jazz")


# ---------- Real database (smoke test) ----------

REAL_DB = Path(__file__).parent / "music.db"


@pytest.mark.skipif(not REAL_DB.exists(), reason="music.db not built; run database.py")
def test_real_database_returns_study_music():
    result = MusicRetriever(str(REAL_DB)).retrieve("I need relaxing music while studying.")

    assert 0 < len(result) <= 5
    for song in result:
        assert song["genre"].lower() in {"lofi", "ambient"} or song["mood"].lower() in {
            "focused", "chill", "relaxed"
        }


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
