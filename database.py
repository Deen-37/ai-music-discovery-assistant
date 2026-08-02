import sqlite3
import csv


def initialize_database():
    """
    Creates the SQLite database and imports songs from the CSV file.
    """

    # Connect to the database (creates it if it doesn't exist).
    connection = sqlite3.connect("music.db")
    cursor = connection.cursor()

    # Create the songs table.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS songs (
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

    # Clear old data so duplicates aren't inserted.
    cursor.execute("DELETE FROM songs")

    # Read the CSV file.
    with open("data/songs.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute("""
                INSERT INTO songs VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
            """, (
                row["id"],
                row["title"],
                row["artist"],
                row["genre"],
                row["mood"],
                row["energy"],
                row["tempo_bpm"],
                row["valence"],
                row["danceability"],
                row["acousticness"]
            ))

    # Save changes and close the database.
    connection.commit()
    connection.close()


if __name__ == "__main__":
    initialize_database()
    print("Database created successfully.")