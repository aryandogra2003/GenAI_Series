# GenAI Series

A collection of hands-on examples exploring LangChain, agents, and retrieval-augmented generation (RAG), plus small Streamlit applications.

## Contents

- `notebooks/` — examples covering prompts, memory, structured output, streaming, agents, search, document loading, text splitting, embeddings, and PDF Q&A.
- `apps/` — Streamlit Q&A and task-management apps, plus a command-line Google search agent.
- `requirements.txt` — Python dependencies used by the examples.

Local datasets, credentials, generated databases, and vector-store files are intentionally excluded from this repository. Add your own permitted sample data locally when following the data-oriented examples.

## Setup

Use Python 3.10 or newer. From the repository root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Add the API keys needed by the example you want to run to `.env`. Never commit `.env` or paste API keys into notebooks.

## Run an app

Start the Groq-powered Q&A app from the repository root:

```powershell
streamlit run apps/1_qna_bot.py
```

For the task-management app, run Streamlit from `apps` so its SQLite database is created alongside the app:

```powershell
Set-Location apps
streamlit run 3_sql_agent.py
```

The Google search agent is a command-line example:

```powershell
python apps/2_google_agent.py
```

The apps use Groq; the Google search agent also requires a Serper API key. Notebooks may require additional provider keys or local services depending on the example.
