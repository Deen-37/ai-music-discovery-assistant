# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

A simple music recommender that matches songs to a listener's vibe.

---

## 2. Intended Use  
# 🎧 Model Card: AI Music Discovery Assistant

## 1. Model Name

**AI Music Discovery Assistant**

A Retrieval-Augmented Generation (RAG) system that recommends songs using a local Large Language Model and a SQLite music database.

---

## 2. Intended Use

### Goal / Task

The AI Music Discovery Assistant recommends songs based on a user's natural language request. Instead of directly generating recommendations, the system first retrieves relevant songs from a SQLite database and then uses a local Llama 3.2 model (through Ollama) to generate recommendations based only on the retrieved songs.

### Who it's for

This project was developed as part of the CodePath Applied AI curriculum to demonstrate Retrieval-Augmented Generation (RAG), local language models, guardrails, and automated evaluation.

### Assumptions

- Users describe their music preferences using natural language.
- The requested songs exist within the project's music database.
- The retrieved songs provide enough context for the language model to generate useful recommendations.

### Intended Use

- Educational demonstrations
- Learning Retrieval-Augmented Generation (RAG)
- AI software engineering portfolio
- Local AI experimentation

### Non-Intended Use

This project is not intended for commercial music recommendation systems or production streaming services. It only recommends songs contained within the project's dataset and should not be considered a replacement for commercial recommendation engines.

---

## 3. How the Model Works

The AI Music Discovery Assistant follows a Retrieval-Augmented Generation (RAG) workflow.

1. The user enters a natural language music request.
2. The MusicRetriever searches a SQLite database using weighted keyword matching and query expansion.
3. The highest-scoring songs are retrieved.
4. The retrieved songs are passed to Llama 3.2 running locally through Ollama.
5. The language model generates recommendations using only the retrieved songs.
6. Guardrails validate the JSON response and verify that recommended songs exist in the retrieved results.
7. Valid recommendations are returned to the user.

Unlike my original project, the language model is not allowed to invent recommendations from general knowledge. Every recommendation must come from the retrieved dataset.

---

## 4. Data

### Dataset

- Approximately 20 songs.
- Stored in a SQLite database generated from the original CSV dataset.
- Each song contains:

  - Title
  - Artist
  - Genre
  - Mood
  - Energy
  - Tempo
  - Valence
  - Danceability
  - Acousticness

### Data Limitations

The dataset is intentionally small for educational purposes. Many genres contain only one or two songs, meaning recommendations are limited by the available data.

---

## 5. Strengths

The current system performs well because:

- Retrieval limits the language model to known songs, reducing hallucinations.
- SQLite provides fast and structured retrieval.
- Running Llama 3.2 locally through Ollama improves privacy and eliminates dependence on cloud APIs.
- Guardrails validate every recommendation before it is returned.
- Automated evaluation makes it easy to identify failures and measure system reliability.
- The modular architecture separates retrieval, prompting, validation, and evaluation into independent components.

---

## 6. Limitations and Bias

Although the system performs well, several limitations remain.

- Recommendations are limited to the songs stored in the local database.
- Retrieval relies on weighted keyword matching rather than semantic vector search.
- Genres with more songs naturally have more opportunities to appear in recommendations.
- The language model occasionally returns malformed JSON, requiring validation through guardrails.
- The small dataset cannot represent the diversity of real-world music preferences.

---

## 7. Evaluation

The project includes an automated evaluation framework.

### Evaluation Process

The Evaluator executes multiple predefined prompts, including requests for:

- Relaxing study music
- Workout music
- Happy songs
- Sad songs
- Jazz
- Sleep music
- Coding music
- Party music

For each test, the system measures:

- Successful retrieval
- Valid JSON generation
- Guardrail validation
- Response time
- Overall pass/fail status

### Results

Most evaluation cases successfully retrieved relevant songs and generated valid recommendations.

The evaluator also exposed several edge cases where the language model produced malformed JSON or inconsistent formatting. These failures demonstrated the value of automated testing and guardrails when building AI applications.

---

## 8. Future Work

Potential improvements include:

- Semantic retrieval using vector embeddings.
- Confidence scoring for recommendations.
- Automatic retry when malformed JSON is generated.
- Larger music datasets.
- REST API integration.
- Web application deployment.
- Personalized recommendation history.

---

## 9. Personal Reflection

The biggest lesson I learned from this project is that building an AI application involves much more than connecting a language model to an interface. The retrieval system, database design, prompt engineering, validation, and automated testing all contribute to producing reliable results.

Using AI tools helped me understand unfamiliar concepts, debug problems, and improve the overall architecture. One particularly valuable suggestion was replacing the original CSV-based retrieval with SQLite, which made the project more realistic and aligned it more closely with modern software engineering practices.

Not every AI suggestion was correct. One recommendation was to use the language model to extract genres and moods before retrieval. In practice, this produced inconsistent outputs that reduced retrieval quality. Through testing, I learned that retrieving directly from the user's natural language request using weighted keyword matching produced more reliable results for this project.

If I continue developing this application, I would replace keyword retrieval with semantic embeddings, expand the dataset, and add a web interface so users can interact with the system through a browser.
**Goal / Task:** VibeFinder suggests songs that fit a user's taste. It takes a
favorite genre, a favorite mood, and a target energy level, then returns the
top 5 songs that best match.

**Who it's for:** This is a classroom project for learning how recommender
systems work. It is not built for real listeners or a real music app.

**Assumptions it makes about the user:**
- The user can name one favorite genre and one favorite mood.
- The user can pick a single energy level they want right now.
- The user's taste can be captured by just those three things.

**Intended use:** Learning, experimenting, and comparing how different user
profiles change the results.

**Non-intended use:** Do not use this for real product recommendations, to judge
an artist's quality, or to make decisions about people. The dataset is tiny and
the rules are simplified, so the results are for practice only.

---

## 3. How the Model Works  

**Algorithm Summary (in plain language):**

VibeFinder gives every song a score, then shows the highest scorers. A song
earns points three ways:

- **Genre match:** if the song's genre is the user's favorite, it gets **+2 points**.
- **Mood match:** if the song's mood is the user's favorite, it gets **+1 point**.
- **Energy closeness:** the closer the song's energy is to the user's target, the
  more points it gets (up to about +1). A song far from the target gets almost none.

The scores are added up and the songs are sorted from highest to lowest. The top 5
are shown, each with the reasons that explain why it scored the way it did.

**What I changed from the starter logic:** I kept the three-part scoring but focused
on making the output clear — each recommendation now shows the song, its score, and
a readable list of reasons, so it's easy to see *why* a song was picked.

---

## 4. Data  

**Data Used:**

- **Size:** 20 songs in the catalog (a CSV file).
- **Features per song:** title, artist, genre, mood, energy, tempo, valence,
  danceability, and acousticness. The current scoring only uses genre, mood, and energy.
- **Genres represented:** 16 different genres, but the spread is uneven — pop and
  lofi have 3 songs each, and most genres (classical, jazz, metal, country, and more)
  have only 1 song.
- **Moods represented:** many moods such as happy, chill, intense, calm, and relaxed.
- **Changes:** I used the provided dataset and did not add or remove songs.
- **What's missing:** With only 20 songs, most genres are barely covered, so users
  with niche tastes have very few real matches. Big parts of real musical taste
  (sub-genres, languages, eras, artist history) are not in the data at all.

---

## 5. Strengths  

**Where the system works well:**

- **Well-covered genres:** Users who like pop or lofi get strong, on-target results,
  because those genres have several songs to choose from.
- **Energy matching works clearly:** High-energy users get loud songs and low-energy
  users get calm songs. This part of the scoring behaved exactly as expected.
- **Aligned tastes shine:** When a user's genre, mood, and energy all point the same
  way (like "Chill Lofi" or "Happy Pop"), the top results match almost perfectly.
- **Explainable:** Every recommendation comes with reasons, so it's easy to understand
  and trust why a song was chosen.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The biggest weakness I found is that the scoring overweights an exact genre match: a genre hit is worth +2.0, while mood (+1.0) and the energy gap (max +1.0) combined can barely tie it, so once a song shares the user's favorite genre it almost always floats to the top regardless of how well the mood or energy actually fit. This creates a filter bubble where the top-5 list collapses onto a single genre and rarely surfaces good cross-genre matches. The problem is worse because the catalog is thin and uneven — only 20 songs across 16 genres, with pop and lofi having 3 songs each and most genres (classical, jazz, metal, country, etc.) having just one, so fans of those niche genres get almost no genre-matched options and are effectively ranked only on the energy gap. The energy calculation itself (`1 - abs(song_energy - target_energy)`) can go negative and is added unconditionally, so it can quietly penalize a strong genre/mood match instead of just rewarding closeness. Together these choices favor mainstream-pop-leaning users and under-serve anyone with niche or mixed tastes.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

### Profiles I tested

1. **Happy Pop** — pop genre, happy mood, high energy (0.8)
2. **Calm Classical** — classical genre, calm mood, low energy (0.2)
3. **EDM Party** — edm genre, party mood, very high energy (0.95)
4. **Chill Lofi** — lofi genre, chill mood, low energy (0.3)

For each one I looked at the top 5 songs and checked whether the genre, mood, and
energy of the results actually matched what the user asked for.

### What surprised me

The biggest surprise was **"Gym Hero" showing up for the Happy Pop user even though
its mood is "intense," not "happy."** In plain language: the system gives a big
bonus (worth 2 points) any time the genre matches, but a matching mood is only worth
1 point. "Gym Hero" is a pop song with very high energy, so it collects the full
genre bonus plus a strong energy score — enough to beat songs that actually fit the
happy mood but belong to a different genre. So a song can rank high just for being
"the right genre and roughly the right energy," even if the feeling is wrong. That's
why an intense workout song keeps landing in a list meant for cheerful pop.

### Comparing the profiles (what changed and why)

- **Happy Pop vs. Calm Classical:** These are near opposites and the outputs flipped
  as expected — Happy Pop returned high-energy pop songs (energy ~0.8), while Calm
  Classical returned quiet, low-energy songs (energy ~0.2). This makes sense because
  the energy target pulls the results toward the user's chosen loudness/intensity.

- **Happy Pop vs. EDM Party:** Both want high energy, so they *share* some songs —
  "Gym Hero" appears in both lists. The difference is the genre bonus: Happy Pop puts
  its own pop songs on top, while EDM Party puts "Desert Mirage" (an edm song) first.
  It makes sense that two high-energy users overlap on the loud songs but diverge on
  which genre wins the top spot.

- **EDM Party vs. Calm Classical:** The clearest contrast — EDM Party's list is full
  of loud, intense songs (energy 0.89–0.97), while Calm Classical's list is full of
  soft, mellow ones (energy 0.18–0.48). This is exactly what the energy preference is
  supposed to do, so the output looks valid.

- **Calm Classical vs. Chill Lofi:** Both are low-energy, so their lists overlap on
  quiet songs like "Spacewalk Thoughts" and "Forest Whisper." But Chill Lofi's own
  genre has three songs in the catalog, so it fills its top 3 with real lofi matches
  and scores them very high (~3.9), while Classical has only one classical song and
  has to fall back to other calm, low-energy songs. This shows how genres with more
  songs in the dataset give the user much stronger, more on-target results.

- **Chill Lofi vs. Happy Pop:** Both are "genre + mood + energy all aligned" cases,
  and both produced clean top-2 results that matched perfectly (lofi/chill for one,
  pop/happy for the other). This confirms the system works best when a user's favorite
  genre is well represented in the catalog.



## 8. Future Work  

**Ideas for Improvement:**

1. **Rebalance the scoring.** The genre bonus (+2) is too strong compared to mood
   (+1). Lowering it, or letting mood matter more, would stop off-mood songs like
   "Gym Hero" from crowding into happy-pop lists.
2. **Add more songs and use more features.** A bigger, more balanced catalog would
   help niche-genre users, and the model could also use tempo, danceability, and
   acousticness — data that already exists but isn't scored yet.
3. **Encourage variety in the top 5.** Right now the list can collapse onto one
   genre. Adding a rule that mixes in some different-but-good matches would make the
   recommendations feel fresher.

---

## 9. Personal Reflection  

**My biggest learning moment** was seeing how much the *weights* matter. Changing a
single number (the +2 genre bonus) completely changed which songs rose to the top.
That's when it clicked that a recommender's "personality" lives in its scoring rules,
not in anything magical.

**Using AI tools** helped me move faster — cleaning up the output formatting, running
several user profiles at once, and spotting the "Gym Hero" pattern. But I still had to
double-check the results myself. I read the actual songs each profile returned and
confirmed the genre, mood, and energy really matched, instead of just trusting that
the code "looked right."

**What surprised me** is how a few simple add-the-points rules can *feel* like a real
recommendation. There's no machine learning here at all, yet the output still seems
like the system "understands" the user. It made me realize that many everyday
recommendations are simpler than they look.

**If I extended this project,** I'd rebalance the scoring, grow the dataset, and add a
diversity rule so the top 5 isn't dominated by one genre. I'd also let users combine
more than one favorite genre or mood, since real taste is rarely just one thing.
