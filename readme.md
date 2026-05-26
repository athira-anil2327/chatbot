# RAG Chatbot using Ollama, LangChain, and Hugging Face

## Overview

This project is a local Retrieval-Augmented Generation (RAG) chatbot built using:

* Ollama for running local LLMs
* LangChain for orchestration
* Hugging Face embeddings
* ChromaDB for vector storage
* PyPDF for PDF loading

The chatbot can read PDF documents, retrieve relevant information, and answer user questions based on the document content.

---

## Features

* Local AI chatbot
* PDF-based question answering
* Semantic search using embeddings
* Vector database retrieval
* Runs completely offline after setup
* Uses Ollama local models

---

## Tech Stack

| Technology   | Purpose           |
| ------------ | ----------------- |
| Python       | Backend language  |
| Ollama       | Local LLM runtime |
| LangChain    | AI orchestration  |
| Hugging Face | Embedding models  |
| ChromaDB     | Vector database   |
| PyPDF        | PDF loading       |
| Torch        | ML acceleration   |

---

## Project Structure

```text
chatbot/
│
├── rag.py
├── sample.pdf
├── requirements.txt
├── .gitignore
├── README.md
├── venv/
└── .git/
```

---

## Installation

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd chatbot
```

---

### 2. Create Virtual Environment

```bash
python3 -m venv venv
```

Activate environment:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install Ollama

Install Ollama from:

[https://ollama.com/](https://ollama.com/)

Pull a model:

```bash
ollama pull llama3
```

---

## Running the Project

Run the chatbot:

```bash
python rag.py
```

---

## Example Questions

* Summarize the document
* What is the main topic?
* Explain chapter 2
* What technologies are mentioned?
* Give a short overview

---

## How RAG Works

```text
PDF
 ↓
Document Loader
 ↓
Text Splitter
 ↓
Embeddings
 ↓
Vector Database
 ↓
Retriever
 ↓
LLM (Ollama)
 ↓
Answer Generation
```

---

## Current Model

This project currently uses:

```text
llama3
```

You can also use:

* mistral
* phi3
* gemma

---

## Future Improvements

* Streamlit UI
* Chat history memory
* Multiple PDF support
* Source citations
* Voice assistant
* FastAPI backend
* React frontend
* Persistent vector storage

---

## Requirements

Main libraries used:

```text
langchain
langchain-community
langchain-ollama
langchain-huggingface
langchain-text-splitters
chromadb
sentence-transformers
pypdf
torch
```

---

## Author

Athira Anil

---

## License

This project is for learning and educational purposes.
