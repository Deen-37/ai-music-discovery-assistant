# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This music recommender uses a content-based filtering approach. Instead of comparing users, it recommends songs by matching their features with a user's preferences. The system prioritizes genre, mood, and energy, then ranks songs based on their overall similarity. This provides personalized recommendations using the attributes available in the dataset.

Song features

Genre
Mood
Energy
Tempo BPM
Valence
Danceability
Acousticness

UserProfile features

Favorite genre
Favorite mood
Target energy

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.How The System Works

This music recommender uses a content-based filtering approach. It compares each song's features with the user's preferences to determine how well they match. The system prioritizes genre, mood, and energy, then assigns each song a score. Finally, it ranks all songs from highest to lowest score and recommends the top results.

Algorithm Recipe
Genre match: +2.0 points
Mood match: +1.0 point
Energy similarity: 1 - abs(song_energy - target_energy)
Total score = Genre score + Mood score + Energy similarity score
Rank songs by total score and return the top recommendations.
Potential Bias

This recommender may over-prioritize genre, causing songs with matching moods or energy but different genres to rank lower. Since it uses only a few song features, it cannot understand lyrics, personal memories, or changing musical tastes.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
============================================================
                   TOP SONG RECOMMENDATIONS                 
============================================================
  Profile: pop / happy / energy 0.8
============================================================

  #1  Sunrise City
      by Neon Echo
      Score: 3.98
      Reasons:
        - Genre match (+2.0)
        - Mood match (+1.0)
        - Energy similarity (+0.98)

  #2  Morning Smile
      by Sunny Lane
      Score: 3.96
      Reasons:
        - Genre match (+2.0)
        - Mood match (+1.0)
        - Energy similarity (+0.96)

  #3  Gym Hero
      by Max Pulse
      Score: 2.87
      Reasons:
        - Genre match (+2.0)
        - Energy similarity (+0.87)

  #4  Rooftop Lights
      by Indigo Parade
      Score: 1.96
      Reasons:
        - Mood match (+1.0)
        - Energy similarity (+0.96)

  #5  City Lights
      by Urban Flow
      Score: 0.99
      Reasons:
        - Energy similarity (+0.99)

============================================================


============================================================
  Profile: rock / energetic / energy 0.9
============================================================

  #1  Storm Runner
      by Voltline
      Score: 2.99
      Reasons:
        - Genre match (+2.0)
        - Energy similarity (+0.99)

  #2  Desert Mirage
      by Sand Pulse
      Score: 1.95
      Reasons:
        - Mood match (+1.0)
        - Energy similarity (+0.95)

  #3  Festival Fire
      by Luna Beats
      Score: 0.99
      Reasons:
        - Energy similarity (+0.99)

  #4  Gym Hero
      by Max Pulse
      Score: 0.97
      Reasons:
        - Energy similarity (+0.97)

  #5  Morning Smile
      by Sunny Lane
      Score: 0.94
      Reasons:
        - Energy similarity (+0.94)

============================================================


============================================================
  Profile: classical / calm / energy 0.2
============================================================

  #1  Silent Memories
      by Velvet Keys
      Score: 2.98
      Reasons:
        - Genre match (+2.0)
        - Energy similarity (+0.98)

  #2  Ocean Breeze
      by Blue Tides
      Score: 1.72
      Reasons:
        - Mood match (+1.0)
        - Energy similarity (+0.72)

  #3  Spacewalk Thoughts
      by Orbit Bloom
      Score: 0.92
      Reasons:
        - Energy similarity (+0.92)

  #4  Forest Whisper
      by Green Meadow
      Score: 0.87
      Reasons:
        - Energy similarity (+0.87)

  #5  Library Rain
      by Paper Lanterns
      Score: 0.85
      Reasons:
        - Energy similarity (+0.85)

============================================================
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



