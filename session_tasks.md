# Parallel Agent Session Tasks

## Session A

**Branch name:** `feature/music-agent-a-tests`

**Worktree directory:** `../music-agent-a`

**Task:** Review and improve the tests for music retrieval.

**Files or folders the agent may write to:** `test_retriever.py` only.

**Files or folders the agent may read but not write to:** All other project files, including retrieval source code, `README.md`, and other tests.

**Commands the agent may run:**
- `python test_retriever.py`
- `pytest test_retriever.py`

**Definition of done:**
- Tests meaningfully cover music retrieval behavior.
- Relevant tests run, and results are reported.
- Only `test_retriever.py` is modified.
- Changes are committed.

## Session B

**Branch name:** `feature/music-agent-b-readme`

**Worktree directory:** `../music-agent-b`

**Task:** Review and improve the project documentation.

**Files or folders the agent may write to:** `README.md` only.

**Files or folders the agent may read but not write to:** All other project files, including source code, tests, and `requirements.txt`.

**Commands the agent may run:**
- `git status`
- `git diff -- README.md`
- `Get-ChildItem`

**Definition of done:**
- Setup instructions and commands match the existing project.
- The project structure and features are documented accurately.
- Only `README.md` is modified.
- Changes are committed.