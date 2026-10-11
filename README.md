# 🎵 AI Music Discovery Assistant

## Overview

The AI Music Discovery Assistant is a Retrieval-Augmented Generation (RAG) application that recommends songs based on a user's natural language request. Instead of allowing the language model to freely generate recommendations, the system first retrieves relevant songs from a SQLite database and then uses a local Large Language Model (Llama 3.2 running through Ollama) to generate personalized recommendations based only on the retrieved data.

The application also includes guardrails that validate the AI's output and an automated evaluation framework that measures the system's reliability across multiple test cases.

This project demonstrates how traditional software engineering practices can be combined with Retrieval-Augmented Generation (RAG), local Large Language Models, and automated evaluation to build a more reliable AI application.

---

# Original Project

This project extends my original CodePath AI project, which was a rule-based music recommendation system built around a CSV dataset. The original application recommended songs using manually designed scoring rules based on genre, mood, and energy.

For this final project, the application was redesigned into a Retrieval-Augmented Generation (RAG) system by introducing:

- SQLite for structured data retrieval
- A local Large Language Model using Ollama (Llama 3.2)
- Guardrails for output validation
- Automated evaluation for reliability testing
- Modular software architecture

---

# Features

- Retrieval-Augmented Generation (RAG)
- SQLite-based music retrieval
- Local LLM integration using Ollama (Llama 3.2)
- Weighted keyword retrieval
- Query expansion
- Guardrails to reduce hallucinations
- Automated evaluation framework
- Structured JSON recommendations
- Modular project architecture

---

# How the System Works

The application follows a Retrieval-Augmented Generation (RAG) workflow.

1. The user enters a natural language music request.
2. `MusicRetriever` expands the request with related keywords (for example, `gym` adds `intense`, `pop`, `edm`; `studying` adds `focused`, `lofi`, `chill`).
3. Every song in the SQLite `songs` table is scored against the expanded request: genre and mood matches add 3 points each, and artist and title matches add 2 points each. Songs with a score of 0 are dropped.
4. The top 5 songs are inserted into a prompt (`src/prompts.py`) that asks the model to recommend the best 3 songs, using only the retrieved songs, and to return only JSON.
5. Llama 3.2 (running locally through Ollama) generates the response.
6. The response is parsed with `json.loads`, and `Guardrails` checks that it is a list, that every item has `title`, `artist`, and `reason`, and that every title is one of the retrieved songs.
7. Valid recommendations are returned as a list. If no songs match the request, a "Sorry, I couldn't find any matching songs." message is returned instead. If the guardrails reject the response, an `{"error": ..., "invalid_titles": [...]}` dictionary is returned.

This approach reduces hallucinations because the language model is restricted to the retrieved songs rather than generating recommendations from general knowledge.

---

# System Architecture

The project is organized into modular components.

- **MusicAgent** (`src/agent.py`) coordinates the complete workflow.
- **MusicRetriever** (`src/retriever.py`) searches the SQLite database.
- **recommendation_prompt** (`src/prompts.py`) builds the prompt sent to the model.
- **LLMClient** (`src/llm.py`) communicates with Ollama (model `llama3.2` by default).
- **Guardrails** (`src/guardrails.py`) validate generated recommendations.
- **Evaluator** (`src/evaluator.py`) runs the complete system against 10 predefined prompts.

The complete architecture diagram is available in:

```
diagrams/architecture.mmd
```

---

# Technologies Used

- Python 3
- SQLite
- Ollama
- Llama 3.2
- JSON
- Mermaid
- Git
- GitHub

---

# Project Structure

```text
ai-music-discovery-assistant/
│
├── data/
│   └── songs.csv            # 20-song catalog (title, artist, genre, mood, audio features)
│
├── diagrams/
│   └── architecture.mmd     # Mermaid architecture diagram
│
├── src/
│   ├── agent.py             # MusicAgent: retrieve -> prompt -> LLM -> guardrails
│   ├── evaluator.py         # Evaluator: runs 10 predefined prompts
│   ├── guardrails.py        # Guardrails: validates the LLM's JSON output
│   ├── llm.py               # LLMClient: wraps the Ollama chat API
│   ├── prompts.py           # recommendation_prompt()
│   └── retriever.py         # MusicRetriever: query expansion + weighted scoring
│
├── database.py              # Builds music.db from data/songs.csv
├── music.db                 # SQLite database (rebuilt by database.py)
├── test_agent.py            # Interactive demo: asks for a request and prints recommendations
├── test_retriever.py        # Prints retrieval results for 5 sample requests (no LLM needed)
├── test_evaluator.py        # Runs the Evaluator
├── README.md
├── model_card.md
└── requirements.txt
```

The `test_*.py` files are standalone scripts run with `python`, not pytest test suites.

---

# Installation

## 1. Clone the repository

```bash
git clone <repository-url>
cd ai-music-discovery-assistant
```

## 2. Create a virtual environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

macOS/Linux

```bash
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Start Ollama

Install [Ollama](https://ollama.com) if you don't already have it, then start the server (leave it running in a separate terminal; the desktop app starts it automatically):

```bash
ollama serve
```

## 5. Download the model

```bash
ollama pull llama3.2
```

## 6. Create the SQLite database

Run all commands from the project root, because the scripts use the relative paths `music.db` and `data/songs.csv`.

```bash
python database.py
```

This creates (or rebuilds) the `songs` table in `music.db` from `data/songs.csv`.

## 7. Run the application

```bash
python test_agent.py
```

The script asks "What kind of music would you like?" and prints the recommendations.

## 8. Check retrieval and run the evaluation

```bash
python test_retriever.py
python test_evaluator.py
```

`test_retriever.py` prints the songs retrieved for 5 sample requests and does not call the LLM. `test_evaluator.py` runs the full pipeline, including Ollama, for 10 sample requests and prints a summary.

---

# Sample Interactions

The LLM's output varies from run to run, so your results may differ from these examples.

## Example 1

### Input

```text
I need relaxing music while studying.
```

### Output

```json
[
  {
    "title": "Library Rain",
    "artist": "Paper Lanterns",
    "reason": "Creates a calm atmosphere that supports concentration while studying."
  },
  {
    "title": "Midnight Coding",
    "artist": "LoRoom",
    "reason": "Provides a relaxing lofi background for focused work."
  },
  {
    "title": "Coffee Shop Stories",
    "artist": "Slow Stereo",
    "reason": "Offers a peaceful jazz atmosphere ideal for studying."
  }
]
```

---

## Example 2

### Input

```text
Play energetic music for the gym.
```

### Output

```json
[
  {
    "title": "Desert Mirage",
    "artist": "Sand Pulse",
    "reason": "An energetic EDM track suitable for high-intensity workouts."
  },
  {
    "title": "Gym Hero",
    "artist": "Max Pulse",
    "reason": "Motivational music designed for exercise."
  },
  {
    "title": "Storm Runner",
    "artist": "Voltline",
    "reason": "Fast-paced rock music that complements gym sessions."
  }
]
```

---

# Design Decisions

Several design decisions were made to improve the reliability and maintainability of the system.

- SQLite was selected instead of reading directly from CSV files because it more closely resembles production software architectures.
- Retrieval-Augmented Generation (RAG) ensures the language model only generates recommendations from retrieved songs instead of inventing songs.
- Weighted keyword matching and query expansion improve retrieval accuracy for natural language requests.
- Guardrails validate AI-generated responses before returning them to the user.
- Prompts are stored separately in `src/prompts.py`, improving maintainability and separating prompt engineering from application logic.
- The project follows a modular architecture that separates retrieval, prompting, validation, evaluation, and AI communication.

---

# Evaluation

The `Evaluator` (`src/evaluator.py`, run with `python test_evaluator.py`) sends 10 predefined prompts through the complete pipeline. They cover studying, gym, happy pop, sadness, jazz with coffee, sleeping, coding, partying, peaceful music, and confident hip hop.

For each prompt, the evaluator:

- Records the response time and prints the result
- Counts a test as **PASS** if the pipeline finishes without raising an exception
- Counts a test as **FAIL** if an exception is raised (for example, when the model returns malformed JSON that `json.loads` cannot parse, or when Ollama is unreachable)

At the end, it prints the number of tests run, passed, and failed, and the average response time.

The evaluator does not score retrieval relevance automatically. A response that the guardrails reject is returned as an error dictionary, not raised as an exception, so it still counts as a PASS. Check the printed results to spot those cases.

Most test cases successfully retrieved relevant songs and generated valid recommendations. Some edge cases produced malformed JSON responses, demonstrating the importance of guardrails and automated evaluation when developing AI-powered applications.

---

# Future Improvements

Potential future enhancements include:

- Semantic search using vector embeddings
- Confidence scoring for recommendations
- Automatic retry when malformed JSON is returned
- Counting guardrail rejections as failures in the evaluator
- Larger music datasets
- REST API integration
- Web-based user interface
- Personalized recommendation history

---

# Reflection

Building this project taught me that creating a reliable AI application involves much more than connecting a language model to an interface. Retrieval, database design, prompt engineering, validation, and automated testing all play important roles in producing accurate and trustworthy results.

Compared to my original rule-based recommender, this project gave me hands-on experience with Retrieval-Augmented Generation (RAG), local language models, SQLite, and modular software engineering. It also showed me the importance of guardrails and evaluation for identifying failures and improving the reliability of AI systems.

---

# Known Issues

- `test_agent.py` contains a stray `a` on the line before `agent = MusicAgent()`, which raises `NameError: name 'a' is not defined` when the script runs. Delete that line before running the demo.
- `requirements.txt` lists `pandas` twice and includes packages the current code doesn't import (`streamlit`, `anthropic`, `python-dotenv`, `pytest`). The only third-party package the application needs is `ollama`.

---

# Additional Documentation

For a detailed discussion of the system's intended use, limitations, evaluation, ethical considerations, and AI collaboration, see:

- `model_card.md`

---

# License

This project was developed for educational purposes as part of the CodePath Applied AI curriculum.
