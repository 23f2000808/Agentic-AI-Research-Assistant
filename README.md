# Agentic AI Research Assistant

## Project Overview

The **Agentic AI Research Assistant** is a production-style agentic AI system developed progressively alongside the **Krish Naik Complete Agentic AI** course. 

The goal of this repository is to learn and implement modern agentic patterns methodically, starting from basic prompt engineering and structured LLM outputs, through autonomous tool-calling agents, memory, and RAG architectures, up to multi-agent collaboration, guardrails, evaluation, and production deployment.

Each milestone introduces new capabilities strictly as they are studied and mastered.

---

## Current Version

**v0.1 - AI Information Extractor**

Initial learning concepts covered in this milestone:
- **Clean Python Project Architecture:** Scalable folder structure with type hints and configuration management.
- **FastAPI Core:** Lightweight API service exposing a `/health` endpoint and interactive OpenAPI documentation.
- **Pydantic Settings:** Safe, typed configuration loading via environment variables (`.env`).
- **LangChain & LLM Foundation:** Configurable Google Gemini integration (`langchain-google-genai`).
- **Structured Output Schema:** Pydantic models ready for structured document/text extraction (`ExtractedInformation`).
- **Separation of Prompts:** System and user prompt templates maintained independently from application business logic.
- **Testing:** Automated test suite with `pytest` and `httpx`.

---

## Long-Term Roadmap

The project is structured around the following progressive learning milestones:

1. **LangChain Basics** *(v0.1 - Current)*: Foundational setup, LLM connectivity, basic prompting.
2. **Structured Output**: Extracting typed Pydantic models from unstructured data with error handling.
3. **Tools**: Custom LangChain tools, schema definition, and tool docstring standards.
4. **LangGraph**: Directed graphs, StateGraph, nodes, edges, and conditional routing.
5. **State & Memory**: Short-term conversational memory, checkpointers, and persistence.
6. **Human-in-the-Loop**: Approval gates, interrupt mechanisms, and user feedback integration.
7. **RAG (Document Parsing & Structure)**: Ingestion pipelines, chunking strategies, embeddings, and vector stores.
8. **Advanced RAG**: Query rewriting, semantic routing, reranking, and hybrid search.
9. **Deep Agents**: Autonomous multi-step research agents with reflection and self-correction.
10. **Multi-Agent Workflow**: Collaboration between Researcher, Analyst, and Writer specialized agents.
11. **Guardrails**: Input/output validation, PII masking, safety filters, and hallucination detection.
12. **LLM Evaluation**: Quantitative metrics, ground truth benchmarks, and automated evaluation frameworks.
13. **Observability**: Distributed tracing, latency tracking, and LLM call instrumentation.
14. **Deployment**: Containerization with Docker, cloud deployment, and production scaling.

> [!NOTE]
> Future modules currently contain only clean package markers (`__init__.py`) or `.gitkeep`. They will be implemented one milestone at a time as learning progresses.

---

## Current Architecture

```
                          ┌────────────────────────┐
                          │   FastAPI Application  │
                          │      (app/main.py)     │
                          └───────────┬────────────┘
                                      │
            ┌─────────────────────────┼────────────────────────┐
            ▼                         ▼                        ▼
┌───────────────────────┐ ┌───────────────────────┐ ┌────────────────────┐
│      API Routes       │ │     Configuration     │ │    Prompt Layer    │
│  app/api/routes/      │ │    (app/config.py)    │ │ app/prompts/       │
│  - /health            │ │  - Pydantic Settings  │ │ - extraction.py    │
│  - /                  │ │  - .env loader        │ │                    │
└───────────────────────┘ └───────────┬───────────┘ └────────────────────┘
                                      │
                                      ▼
                        ┌───────────────────────────┐
                        │        LLM Service        │
                        │    (app/agents/llm.py)    │
                        │ - ChatGoogleGenerativeAI  │
                        │ - Configurable Provider   │
                        └─────────────┬─────────────┘
                                      │
                                      ▼
                        ┌───────────────────────────┐
                        │      Structured Model     │
                        │ (app/models/extraction.py)│
                        │ - ExtractedInformation    │
                        └───────────────────────────┘
```

---

## Project Structure

```
agentic-research-assistant/
│
├── README.md               # Project documentation and roadmap
├── .gitignore              # Ignored files (venv, secrets, cache)
├── .env.example            # Template for environment variables
├── requirements.txt        # Minimal required Python dependencies
├── pyproject.toml          # Project configuration and metadata
│
├── app/                    # Main application package
│   ├── __init__.py
│   ├── main.py             # FastAPI app initialization & entry point
│   ├── config.py           # Pydantic Settings configuration loader
│   │
│   ├── api/                # API layer
│   │   ├── __init__.py
│   │   └── routes/         # API endpoint routers
│   │       ├── __init__.py
│   │       └── health.py   # Health check endpoint
│   │
│   ├── agents/             # Agent definitions & LLM connections
│   │   ├── __init__.py
│   │   └── llm.py          # Google Gemini LLM factory
│   │
│   ├── graph/              # LangGraph workflows (Milestone 4)
│   │   └── __init__.py
│   │
│   ├── tools/              # Custom agent tools (Milestone 3)
│   │   └── __init__.py
│   │
│   ├── rag/                # RAG retrievers & indexers (Milestone 7-8)
│   │   └── __init__.py
│   │
│   ├── memory/             # State & memory management (Milestone 5)
│   │   └── __init__.py
│   │
│   ├── guardrails/         # Input/output guardrails (Milestone 11)
│   │   └── __init__.py
│   │
│   ├── evaluation/         # LLM benchmarks & evals (Milestone 12)
│   │   └── __init__.py
│   │
│   ├── models/             # Pydantic models & schemas
│   │   ├── __init__.py
│   │   └── extraction.py   # ExtractedInformation schema
│   │
│   └── prompts/            # Prompt templates & instructions
│       ├── __init__.py
│       └── extraction.py   # Extraction prompts
│
├── data/                   # Data storage for documents & evals
│   ├── documents/          # Source documents for RAG (.gitkeep)
│   └── evaluation/         # Evaluation datasets (.gitkeep)
│
├── tests/                  # Test suite
│   ├── __init__.py
│   └── test_health.py      # Health endpoint unit test
│
├── notebooks/              # Jupyter notebooks for experiments (.gitkeep)
├── scripts/                # Utility & maintenance scripts (.gitkeep)
└── docker/                 # Container configuration files (.gitkeep)
```

---

## Setup & Installation

### 1. Prerequisites
- **Python 3.11** or **3.12** is recommended.
- Windows OS (PowerShell or Command Prompt).

### 2. Create the Virtual Environment
Open PowerShell or Command Prompt in the project root:

```powershell
# Using Python 3.11 directly via Python launcher
py -3.11 -m venv .venv
```

*(or `python -m venv .venv` if your default Python is 3.11)*

### 3. Activate the Virtual Environment

**In PowerShell:**
```powershell
.venv\Scripts\Activate.ps1
```

> If you encounter an execution policy error in PowerShell, run:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

**In Command Prompt (CMD):**
```cmd
.venv\Scripts\activate.bat
```

### 4. Install Dependencies
```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Copy `.env.example` to `.env`:

**In PowerShell:**
```powershell
Copy-Item .env.example .env
```

**In CMD:**
```cmd
copy .env.example .env
```

Open `.env` and set your Google Gemini API key:
```ini
GOOGLE_API_KEY=your_actual_api_key_here
MODEL_NAME=gemini-2.5-flash
APP_NAME=agentic-research-assistant
DEBUG=False
```

> [!CAUTION]
> Never commit `.env` or expose your API keys. `.env` is listed in `.gitignore`.

### 6. Run the Application
Start the FastAPI server with Uvicorn:

```powershell
uvicorn app.main:app --reload
```

The server will start at:
- **Root:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Health Check:** [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)
- **Interactive Swagger Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 7. Run Tests
Verify system integrity using `pytest`:

```powershell
pytest
```

---

## Development Philosophy

This project strictly adheres to the progressive learning cycle:

$$\text{Watch} \longrightarrow \text{Understand} \longrightarrow \text{Implement} \longrightarrow \text{Modify} \longrightarrow \text{Test} \longrightarrow \text{Integrate} \longrightarrow \text{Commit}$$

- **One concept at a time**: No premature implementations of future course topics.
- **Clean modular code**: Type annotations, minimal abstractions, and clear docstrings.
- **Test-driven verification**: Every component is tested and verified before progressing.
