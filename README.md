# 🔎 LangChain - Chat with Search using Agents & Tools

A conversational AI chatbot built with **LangChain Agents**, **Groq LLM**, and **Streamlit** that uses intelligent tools to search the web, Wikipedia, and Arxiv in real time.

## ✨ Features

- 🤖 **LangChain ReAct Agent** — Reasons and acts step-by-step to answer questions
- 🛠️ **Multiple Tools** — Web search, Wikipedia, and Arxiv all wired into the agent
- ⚡ **Groq LLM** — Ultra-fast inference using `llama-3.1-8b-instant`
- 💬 **Streamlit UI** — Clean, interactive chat interface with live agent thoughts

---

## 🤖 How the Agent Works

This project uses a **ReAct (Reasoning + Acting) Agent** from LangChain.

The agent follows this loop to answer every question:

```
Question → Thought → Action (Tool) → Observation → Thought → Final Answer
```

### Example:
```
Question: What is the latest research on transformers?

Thought: I should search Arxiv for recent papers on transformers.
Action: Arxiv
Action Input: "transformer neural network 2024"
Observation: [Arxiv results...]

Thought: I now know the final answer.
Final Answer: The latest research on transformers includes...
```

The agent **decides on its own** which tool to use based on the question.

---

## 🛠️ Tools

The agent has access to 3 tools:

| Tool | Source | Purpose |
|------|--------|---------|
| 🔍 **DuckDuckGoSearchRun** | DuckDuckGo | Search the live web for current information |
| 📖 **WikipediaQueryRun** | Wikipedia API | Fetch summaries from Wikipedia articles |
| 📄 **ArxivQueryRun** | Arxiv API | Search academic and research papers |

---

## 📦 Requirements

```
streamlit
langchain
langchain-groq
langchain-community
langchain-core
duckduckgo-search
arxiv
wikipedia
python-dotenv
```

---

## 📁 Project Structure

```
├── app.py              # Main Streamlit app with Agent & Tools
├── .env                # API keys (never commit this!)
├── .gitignore          # Ignores .env and venv
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [LangChain](https://www.langchain.com/) | Agent, Tools & chain framework |
| [Groq](https://console.groq.com/) | LLM inference (Llama 3.1) |
| [Streamlit](https://streamlit.io/) | Frontend UI |
| [DuckDuckGo](https://duckduckgo.com/) | Live web search tool |
| [Wikipedia API](https://www.mediawiki.org/wiki/API) | Wikipedia search tool |
| [Arxiv API](https://arxiv.org/help/api) | Academic paper search tool |

---


## 🙌 Acknowledgements

- [LangChain](https://www.langchain.com/)
- [Groq](https://groq.com/)
- [Streamlit](https://streamlit.io/)
