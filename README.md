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
2. The MusicRetriever searches a SQLite database using weighted keyword matching and query expansion.
3. The highest-ranked songs are retrieved.
4. The retrieved songs are inserted into a prompt.
5. Llama 3.2 (running locally through Ollama) generates recommendations using only the retrieved songs.
6. Guardrails validate the generated JSON response.
7. Valid recommendations are returned to the user.

This approach reduces hallucinations because the language model is restricted to the retrieved songs rather than generating recommendations from general knowledge.

---

# System Architecture

The project is organized into modular components.

- **MusicAgent** coordinates the complete workflow.
- **MusicRetriever** searches the SQLite database.
- **LLMClient** communicates with Ollama.
- **Guardrails** validate generated recommendations.
- **Evaluator** automatically tests the complete system.

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
├── assets/
├── data/
│   └── songs.csv
│
├── diagrams/
│   └── architecture.mmd
│
├── src/
│   ├── agent.py
│   ├── evaluator.py
│   ├── guardrails.py
│   ├── llm.py
│   ├── prompts.py
│   └── retriever.py
│
├── database.py
├── music.db
├── test_agent.py
├── test_retriever.py
├── test_evaluator.py
├── README.md
├── model_card.md
└── requirements.txt
```

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

```bash
ollama serve
```

## 5. Download the model

```bash
ollama pull llama3.2
```

## 6. Create the SQLite database

```bash
python database.py
```

## 7. Run the application

```bash
python test_agent.py
```

## 8. Run the evaluation

```bash
python test_retriever.py
python test_evaluator.py
```

---

# Sample Interactions

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
- Prompts are stored separately in `prompts.py`, improving maintainability and separating prompt engineering from application logic.
- The project follows a modular architecture that separates retrieval, prompting, validation, evaluation, and AI communication.

---

# Evaluation

The system includes an automated evaluation framework that executes multiple predefined prompts covering different recommendation scenarios.

The evaluation checks:

- Retrieval accuracy
- JSON validity
- Guardrail validation
- Response time
- End-to-end functionality

Most test cases successfully retrieved relevant songs and generated valid recommendations. Some edge cases produced malformed JSON responses, demonstrating the importance of guardrails and automated evaluation when developing AI-powered applications.

---

# Future Improvements

Potential future enhancements include:

- Semantic search using vector embeddings
- Confidence scoring for recommendations
- Automatic retry when malformed JSON is returned
- Larger music datasets
- REST API integration
- Web-based user interface
- Personalized recommendation history

---

# Reflection

Building this project taught me that creating a reliable AI application involves much more than connecting a language model to an interface. Retrieval, database design, prompt engineering, validation, and automated testing all play important roles in producing accurate and trustworthy results.

Compared to my original rule-based recommender, this project gave me hands-on experience with Retrieval-Augmented Generation (RAG), local language models, SQLite, and modular software engineering. It also showed me the importance of guardrails and evaluation for identifying failures and improving the reliability of AI systems.

---

# Additional Documentation

For a detailed discussion of the system's intended use, limitations, evaluation, ethical considerations, and AI collaboration, see:

- `model_card.md`

---

# License

This project was developed for educational purposes as part of the CodePath Applied AI curriculum.
