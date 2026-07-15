
# Basic RAG Pipeline

A beginner-friendly implementation of a **Retrieval-Augmented Generation (RAG)** pipeline using **Python**, **LangChain**, **ChromaDB**, **HuggingFace Embeddings**, and **DeepSeek/Gemini**. This project demonstrates the complete RAG workflow—from loading PDF documents to generating context-aware answers with a Large Language Model (LLM).

> **Note:** This project is part of my learning journey of building AI-powered applications and is intended to understand the core concepts behind RAG systems by building them from scratch.

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#%EF%B8%8F-architecture)
- [Project Structure](#-project-structure)
- [How It Works](#%EF%B8%8F-how-it-works)
- [Installation](#-installation)
- [Usage](#%EF%B8%8F-usage)
- [Example](#-example)
- [Technologies Used](#%EF%B8%8F-technologies-used)
- [Future Improvements](#-future-improvements)
- [License](#-license)
- [Author](#%E2%80%8D-author)

---

## 📌 Overview

Retrieval-Augmented Generation (RAG) improves the quality of Large Language Model responses by retrieving relevant information from external documents before generating an answer.

This project demonstrates the fundamental RAG pipeline using a PDF as the knowledge source. The document is loaded, split into smaller chunks, converted into vector embeddings, stored in a vector database, and retrieved whenever a user asks a question. The retrieved context is then provided to an LLM to generate an accurate response.

The primary goal of this project is to understand how each component of a RAG system works together rather than relying on a pre-built framework.

---

## ✨ Features

- Load PDF documents
- Split documents into semantic chunks
- Generate vector embeddings using HuggingFace
- Store embeddings in ChromaDB
- Retrieve relevant document chunks
- Generate answers using an LLM
- Modular and beginner-friendly code structure
- Easy to extend for future RAG improvements

---

## 🏗️ Architecture

```text
                PDF Document
                      │
                      ▼
               PyPDFLoader
                      │
                      ▼
    RecursiveCharacterTextSplitter
                      │
                      ▼
       HuggingFace Embeddings
          (all-MiniLM-L6-v2)
                      │
                      ▼
                 ChromaDB
                      │
             User Question
                      │
                      ▼
          Similarity Search
                      │
                      ▼
     Retrieved Context + Prompt
                      │
                      ▼
      DeepSeek / Gemini (LLM)
                      │
                      ▼
              Generated Answer
```

---

## 📂 Project Structure

```text
basic-rag-pipeline/
│
├── data/
│   └── sample.pdf
│
├── db/
│
├── src/
│   ├── load_pdf.py
│   ├── split_documents.py
│   ├── create_embeddings.py
│   ├── build_vector_db.py
│   ├── retrieve.py
│   ├── rag_pipeline.py
│   └── config.py
│
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

> The `db/` directory contains the generated Chroma vector database and is not intended to be committed to GitHub.

---

## ⚙️ How It Works

1. Load the PDF using **PyPDFLoader**
2. Split the document into manageable chunks using **RecursiveCharacterTextSplitter**
3. Convert each chunk into vector embeddings using **all-MiniLM-L6-v2**
4. Store the embeddings inside **ChromaDB**
5. Accept a user's question
6. Retrieve the most relevant document chunks
7. Provide the retrieved context to the LLM
8. Generate and return the final answer

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/sachin508508/basic_RAG_Pipeline.git
cd basic_RAG_Pipeline
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file in the project root.

Example:

```env
DEEPSEEK_API_KEY=your_deepseek_api_key
GEMINI_API_KEY=your_gemini_api_key
```

---

## ▶️ Usage

Place your PDF inside the `data/` folder.

Run the RAG pipeline:

```bash
python src/rag_pipeline.py
```

Ask a question related to the PDF.

Example:

```
What are the main responsibilities of a Delivery Data Analyst?
```

The application retrieves the most relevant document chunks and generates an answer using the selected LLM.

---

## 💡 Example

### User Question

```
What is Retrieval-Augmented Generation?
```

### Retrieved Context

```
RAG combines external knowledge retrieval with Large Language Models
to generate more accurate and grounded responses.
```

### Generated Answer

```
Retrieval-Augmented Generation (RAG) is a technique that retrieves
relevant information from external knowledge sources and provides it
to a Large Language Model before generating an answer. This helps
reduce hallucinations and improves response accuracy.
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.13 | Programming Language |
| LangChain | LLM Orchestration |
| ChromaDB | Vector Database |
| HuggingFace Embeddings | Generate Vector Embeddings |
| all-MiniLM-L6-v2 | Embedding Model |
| PyPDFLoader | PDF Loading |
| RecursiveCharacterTextSplitter | Document Chunking |
| DeepSeek API | Large Language Model |
| Gemini API | Alternative LLM |
| python-dotenv | Environment Variable Management |

---

## 🚧 Future Improvements

This project intentionally focuses on the fundamentals of Retrieval-Augmented Generation. Possible future enhancements include:

- Support multiple PDF documents
- Configurable chunk size and overlap
- Configurable Top-K retrieval
- Switch between multiple embedding models
- Support multiple LLM providers
- Command-line interface (CLI)
- Better logging and error handling
- Streamlit web interface
- Docker support
- Unit testing

Advanced RAG techniques such as Hybrid Search, Reranking, LangGraph, Graph RAG, and RAG Evaluation are intentionally left for future dedicated projects.

---

## 📜 License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

---

## 👨‍💻 Author

**Sachin S**

GitHub: https://github.com/sachin508508

---

## ⭐ Acknowledgements

This project was built as part of my AI Engineering learning journey to understand the fundamentals of Retrieval-Augmented Generation (RAG), vector databases, embeddings, and Large Language Models through hands-on implementation.
