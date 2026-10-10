# LaunchCode Agent Sandbox Setup

## 1. Build the Docker Image

```bash
docker build -t music-agent-sandbox .
```

## 2. Run the Container

From the project root in PowerShell:

```powershell
docker run --rm -it -v "${PWD}:/workspace" music-agent-sandbox
```

- **Mount:** The project folder is mounted at `/workspace`.
- **Network:** Default Docker networking is enabled so Claude Code can connect to its service.
- **Persistence:** Changes made in `/workspace` persist on the host. Temporary files in `/tmp` are container-local.

## 3. Smoke Test

**Prompt given to Claude Code:**

> Inspect the repository structure and summarize its main components. Do not modify any existing files. Write the summary to `/workspace/agent-summary.md`.

**Result:** Claude Code connected successfully. The smoke test is complete once `agent-summary.md` is created and its contents are verified.

## 4. Security Decisions

- Mount only the project folder, not the entire host home directory.
- Do not include real credentials, secrets, or `.env` values in the image.
- Use `/tmp` for temporary work that does not need to persist.
- Network access is enabled for Claude Code connectivity. This allows normal outbound networking, so access is not restricted to Claude Code alone.
- The container provides filesystem isolation, but it is not a guarantee against every security risk.

## 5. Project Stack

- **Language:** Python 3.12
- **Dependencies:** Installed using `pip` and `requirements.txt`
- **Database:** SQLite
- **AI model:** Llama 3.2 through Ollama
- **Agent tools:** Claude Code and OpenCode
