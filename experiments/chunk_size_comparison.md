# Chunk Size Comparison Experiment

## 1. Objective

This experiment evaluates how different chunk sizes affect retrieval quality and final answer quality in a Retrieval-Augmented Generation (RAG) pipeline.

Only `CHUNK_SIZE` was changed between experiments. All other configuration values, evaluation questions, and `TOP_K` remained constant.

---

## 2. Dataset and Fixed Configuration

**Document:** *Adoption and Ecosystem Health: A Longitudinal Analysis of Open-Source Multi-Agent Frameworks*
**File:** `data/data_file_RAG.pdf`
**Pages:** 24
**Topic:** Open-source AI agent frameworks and ecosystem health

| Configuration   | Value                             |
| --------------- | --------------------------------- |
| Chunk Overlap   | 200 characters                    |
| Top K           | 3                                 |
| Embedding Model | `all-MiniLM-L6-v2`                |
| Text Splitter   | Recursive Character Text Splitter |

### Evaluation Dataset

The same 10 evaluation questions were used for both experiments. The questions cover:

* Direct factual retrieval
* Definitions
* Explanations
* Cross-section reasoning
* Unanswerable questions

The full evaluation questions are stored in:

`evaluation_questions.json`

---

## 3. Evaluation Methodology

### Retrieval Quality

Measures whether the retrieved chunks contain enough relevant information to answer the question.

| Score   | Meaning                                                                         |
| ------- | ------------------------------------------------------------------------------- |
| Good    | Sufficient relevant information was retrieved.                                  |
| Partial | Some relevant information was retrieved, but important information was missing. |
| Poor    | The retrieved context did not contain the required information.                 |

### Answer Quality

Measures whether the final LLM answer is correct and sufficiently complete based on the retrieved context.

| Score   | Meaning                                                   |
| ------- | --------------------------------------------------------- |
| Good    | Correct and sufficiently complete.                        |
| Partial | Partially correct or incomplete.                          |
| Poor    | Incorrect, unsupported, or failed to answer the question. |

Each experiment was evaluated across 10 questions, resulting in a maximum score of 30 for both retrieval quality and answer quality.

---

# 4. Experiment A: 500-Character Chunks

### Configuration

```text
CHUNK_SIZE = 500
CHUNK_OVERLAP = 200
TOP_K = 3
```

### Dataset Statistics

| Metric       | Value |
| ------------ | ----: |
| Total Pages  |    24 |
| Total Chunks |   176 |

### Results

| Metric                      |           Result |
| --------------------------- | ---------------: |
| Retrieved Context Relevance | 28 / 30 (93.33%) |
| Final Answer Quality        | 29 / 30 (96.67%) |

### Observations

* Retrieved context was generally focused and relevant.
* Most questions received sufficient context.
* Some questions requiring information from multiple sections were occasionally incomplete.
* The unanswerable question was correctly handled.

---

# 5. Experiment B: 1000-Character Chunks

### Configuration

```text
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K = 3
```

### Dataset Statistics

| Metric       | Value |
| ------------ | ----: |
| Total Pages  |    24 |
| Total Chunks |    76 |

### Results

| Metric                      |           Result |
| --------------------------- | ---------------: |
| Retrieved Context Relevance | 26 / 30 (86.67%) |
| Final Answer Quality        | 29 / 30 (96.67%) |

### Observations

* The larger chunk size significantly reduced the total number of chunks.
* Retrieval relevance was lower than with 500-character chunks.
* Final answer quality remained unchanged.
* Some questions requiring information from multiple sections had insufficient retrieved context.

---

# 6. Experiment Comparison

| Metric                      | 500-Character Chunks | 1000-Character Chunks |
| --------------------------- | -------------------: | --------------------: |
| Total Chunks                |                  176 |                    76 |
| Retrieved Context Relevance |           **93.33%** |                86.67% |
| Final Answer Quality        |           **96.67%** |            **96.67%** |

### Result Files

* [Experiment Overview](./results/Experiment_Overview.csv)
* [Experiment Summary](./results/Experiment_Summary.csv)
* [Detailed Evaluation Results](./results/Detailed_Evaluation.csv)

---

## 7. Conclusion

For this document and evaluation setup, **500-character chunks performed better for retrieval**, achieving **93.33%** compared with **86.67%** for 1000-character chunks.

However, both configurations achieved the same **96.67% final answer quality**.

This suggests that smaller chunks provided more focused retrieval, while larger chunks significantly reduced the number of stored chunks without improving final answer quality. Therefore, the 500-character configuration was the better choice for retrieval quality in this experiment.

However, further experiments with different chunk sizes, overlap values, and `TOP_K` values are required before determining the optimal configuration for the RAG pipeline.

---

## 8. Reproducibility

The evaluation workflow:

1. Loads the fixed questions from `evaluation_questions.json`.
2. Retrieves relevant chunks for each question.
3. Generates an answer using the RAG pipeline.
4. Compares the retrieved context and generated answer with the expected answer.
5. Stores the evaluation results.

The evaluation script is:

`evaluate_rag.py`

This workflow allows the same evaluation questions to be reused for future RAG configuration experiments.
