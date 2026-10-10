# Repository Summary: AI Music Discovery Assistant

A small Python app that recommends songs using Retrieval-Augmented Generation (RAG). It searches a local SQLite song catalog with keywords, sends the matching songs to a local Llama 3.2 model (through Ollama) to pick and explain the best 3, and checks that the model only named songs it was given.

## Layout

```
.
├── src/
│   ├── agent.py        # MusicAgent: runs the whole pipeline
│   ├── retriever.py    # MusicRetriever: keyword-expanded, weighted SQLite search
│   ├── llm.py          # LLMClient: wrapper around ollama.chat (default model "llama3.2")
│   ├── prompts.py      # recommendation_prompt(): asks for JSON-only top-3 picks
│   ├── guardrails.py   # Guardrails.validate(): checks JSON shape and that every title was retrieved
│   ├── evaluator.py    # Evaluator: runs 10 fixed prompts, reports pass/fail and timing
│   └── main.py         # Old CLI from the original rule-based recommender (see Issues)
├── database.py         # Loads data/songs.csv into music.db (songs table)
├── data/songs.csv      # 20-song catalog: genre, mood, energy, tempo, valence, etc.
├── music.db            # Prebuilt SQLite database (committed)
├── diagrams/architecture.mmd  # Mermaid architecture diagram
├── test_agent.py       # Interactive script: asks for a request, prints recommendations
├── test_retriever.py   # Script: prints retrieval results for 5 sample prompts
├── test_evaluator.py   # Script: runs Evaluator().run()
├── README.md / model_card.md  # Project docs and model card
├── requirements.txt    # anthropic, pandas, python-dotenv, ollama, pytest, streamlit
├── assets/             # Empty
└── Dockerfile, docker-entrypoint.sh, settings.json, statusline.sh  # Not tracked in git (see below)
```

## How a request flows

1. **Data setup:** running `database.py` (re)creates the `songs` table in `music.db` from `data/songs.csv`.
2. **Retrieval** (`MusicRetriever.retrieve`): loads every row, lowercases the query and adds synonyms from `QUERY_MAP` (for example, "gym" becomes intense/pop/edm). It then scores each song by substring matches: genre +3, mood +3, artist +2, title +2. It returns the top 5 songs with a score above 0.
3. **Prompting** (`recommendation_prompt`): puts the retrieved songs (title, artist, genre, mood) into a prompt that tells the model to return only a JSON list of `{title, artist, reason}`.
4. **Generation** (`LLMClient.generate`): sends one user message through `ollama.chat`.
5. **Guardrails** (`Guardrails.validate`): the response must be a list, every item needs `title`, `artist` and `reason`, and every title must be one of the retrieved songs. If any check fails, it returns an error dict.
6. **Output:** `MusicAgent.recommend` returns the list of recommendations, an error dict, or a "no matching songs" message.

## Evaluation and tests

- `Evaluator` runs 10 hard-coded prompts through the agent. It counts a test as passed whenever no exception is raised, so a guardrail-failure dict or a "no songs" message still counts as a pass.
- The `test_*.py` files are plain scripts with no `test_` functions or asserts. `pytest` would run them at import time, and `test_agent.py` would wait for `input()`.

## Infrastructure files (untracked)

- `Dockerfile`: a python:3.12-slim dev container with Node, Claude Code, OpenCode and ngrok, plus shell aliases. Its `ai-course` prompt suggests it is a course environment.
- `docker-entrypoint.sh`: keeps Claude Code credentials across container restarts by syncing them to a `/claude-auth` volume.
- `settings.json` / `statusline.sh`: Claude Code status-line configuration copied into `/root/.claude`.

## Working-tree state

`git status` shows 16 tracked files as modified. Ignoring line endings, the only real change is in `test_agent.py`, so the rest is almost certainly a CRLF/LF difference.

## Issues noticed (not fixed: the task said not to modify files)

- **`test_agent.py`:** the uncommitted change adds a stray `a` line before `agent = MusicAgent()`, which raises `NameError` when the script runs.
- **`src/main.py`:** imports `src.recommender` / `recommender`, and neither exists. It is leftover code from the original rule-based project and will fail on import.
- **`src/agent.py`:** calls `json.loads(response)` without error handling, so any output that isn't JSON (for example, wrapped in markdown fences) raises an exception.
- **`Guardrails.validate`:** checks titles but not whether each artist matches its title.
- **Retriever:** uses plain substring matching, which can give false positives. For example, the mood "chill" would match inside "chilling".
- **`requirements.txt`:** lists `anthropic`, `python-dotenv` and `streamlit`, but the code never uses them.
- **`diagrams/architecture.mmd`:** contains a typo in a comment (`--------go--`).
- **`music.db`:** is committed even though `database.py` regenerates it. Also, `.gitignore` doesn't exclude it.
