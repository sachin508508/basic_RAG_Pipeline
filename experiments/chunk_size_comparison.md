# Chunk Size Comparison Experiment

## Experiment Objective

The objective of this experiment is to study how different chunk sizes affect the performance of a Retrieval-Augmented Generation (RAG) pipeline.

In this experiment, the chunk size will be changed while keeping the other configuration values constant. The retrieved results will then be evaluated using a fixed set of questions.

The goal is to understand how chunk size affects:

* The number of chunks created from the document
* The quality and relevance of retrieved chunks
* The context provided to the language model
* The final answer quality

---

## PDF Used

**Document:** Adoption and Ecosystem Health: A Longitudinal Analysis of Open-Source Multi-Agent Frameworks

**File:** `data_file_RAG.pdf`

**Number of pages:** 24
**Total chunks created:** 176

**Topic:** Open-source AI agent frameworks and ecosystem health

The document analyzes 15 open-source AI agent frameworks using metrics such as GitHub stars, contributors, cross-ecosystem contribution, and contributor retention.

---

## Fixed Configuration

The following configuration values remain unchanged throughout the experiment:

| Configuration   | Value                             |
| --------------- | --------------------------------- |
| Chunk Overlap   | 200 characters                    |
| Top K           | 3                                 |
| Embedding Model | `all-MiniLM-L6-v2`                |
| LLM             | Gemini                            |
| Temperature     | 0.4                               |
| Maximum Tokens  | 1024                              |
| Text Splitter   | Recursive Character Text Splitter |
| Document        | `data_file_RAG.pdf`               |

Only the `CHUNK_SIZE` value will be changed between experiments.

---

## Evaluation Questions

The same evaluation questions will be used for every future chunk-size experiment to ensure a consistent comparison between different chunking strategies.

### Question 1 — Direct Factual

How many open-source AI agent framework repositories were analyzed in the study?

**Expected answer:** 15 repositories.

---

### Question 2 — Direct Factual

What was the total number of unique human code contributors identified across all 15 repositories after filtering out bot accounts?

**Expected answer:** 12,594 unique human code contributors.

---

### Question 3 — Definition

What is the contributor density ratio, and how is it calculated?

**Expected answer:** The contributor density ratio is the number of total code contributors per 1,000 GitHub stars. It is calculated as:

`Total Contributors / Total Stars × 1,000`

---

### Question 4 — Explanation

Why does the study argue that GitHub star counts alone are not a reliable measure of actual adoption?

**Expected answer:** Star counts primarily measure visibility or awareness and may be affected by hype cycles, launch effects, anomalous activity, or coordinated starring. They do not necessarily represent active engagement or actual code contribution.

---

### Question 5 — Information from Different Sections

Which framework had the highest contributor density ratio, and how does this relate to the framework's position in the awareness-versus-adoption analysis?

**Expected answer:** Pydantic AI had the highest contributor density ratio at 42.3 contributors per 1,000 stars. It was classified as a Quiet Compounder, meaning it had relatively lower awareness but comparatively strong contributor engagement.

---

### Question 6 — Information from Different Sections

Why is LangChain considered a shared infrastructure or bridge within the open-source AI agent framework ecosystem?

**Expected answer:** LangChain attracted approximately 82.5% of cross-ecosystem contributors and appeared in many cross-framework contributor pairings. Its composable components are also used by or integrated with other frameworks, allowing contributors to engage across multiple ecosystems.

---

### Question 7 — Explanation

What does the study reveal about contributor retention during the first 30 to 90 days after a contributor's initial contribution?

**Expected answer:** The steepest decline in contributor retention occurs during the first 30 days. Retention may increase somewhat by 60 or 90 days as contributors have more time to return, but it generally stabilizes after approximately 90 days.

---

### Question 8 — Cross-Section Reasoning

AutoGPT had very high visibility but relatively low contributor retention. What does this comparison suggest about the difference between popularity and sustained adoption?

**Expected answer:** High visibility or popularity does not necessarily lead to sustained community engagement. AutoGPT attracted significant attention and stars, but its contributor retention was relatively low, showing that initial popularity and long-term adoption are different measures.

---

### Question 9 — Direct Factual

Which framework had the lowest contributor density ratio in the dataset, and what was its ratio?

**Expected answer:** MetaGPT had the lowest contributor density ratio at 3.9 contributors per 1,000 stars.

---

### Question 10 — Unanswerable from the PDF

What was the exact average response time, in hours, for maintainers to review and merge a first-time contributor's pull request in the LangChain repository?

**Expected answer:** This information cannot be determined from the PDF.

The PDF discusses factors such as review speed, PR merge rate, and responsiveness as potentially important factors in contributor retention, but it does not provide the exact average response time for LangChain.

---
# Chunk Size Comparison Experiment

## Experiment Objective

The objective of this experiment is to evaluate how different chunk sizes affect retrieval quality and final answer quality in a RAG pipeline.

The same PDF, evaluation questions, chunk overlap, and `TOP_K` value were used in both experiments. Only the chunk size was changed.

---

## PDF Used

**Document:** Adoption and Ecosystem Health: A Longitudinal Analysis of Open-Source Multi-Agent Frameworks

**File:** `data/data_file_RAG.pdf`

**Total Pages:** 24

---

## Fixed Configuration

| Configuration   | Value                             |
| --------------- | --------------------------------- |
| Chunk Overlap   | 200 characters                    |
| Top K           | 3                                 |
| Embedding Model | `all-MiniLM-L6-v2`                |
| Text Splitter   | Recursive Character Text Splitter |

---

# Experiment A: 500-Character Chunks

## Configuration

```text
CHUNK_SIZE = 500
CHUNK_OVERLAP = 200
TOP_K = 3
```

## Dataset Statistics

| Metric                 | Value |
| ---------------------- | ----- |
| Total Pages            | 24    |
| Total Chunks           | 176   |
| Total Retrieved Chunks | 3     |

## Results

| Metric                      | Result           |
| --------------------------- | ---------------- |
| Retrieved Context Relevance | 27 / 30 (90%)    |
| Final Answer Quality        | 29 / 30 (96.67%) |

### Observations

* Most questions retrieved relevant context.
* Questions requiring information from multiple sections were occasionally incomplete.
* The unanswerable question was correctly handled.
* The retrieved context was generally focused and relevant.

---

# Experiment B: 1000-Character Chunks

## Configuration

```text
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K = 3
```

## Dataset Statistics

| Metric                 | Value |
| ---------------------- | ----- |
| Total Pages            | 24    |
| Total Chunks           | 76    |
| Total Retrieved Chunks | 3     |

## Results

| Metric                      | Result           |
| --------------------------- | ---------------- |
| Retrieved Context Relevance | 25 / 30 (83.33%) |
| Final Answer Quality        | 29 / 30 (96.67%) |

### Observations

* The larger chunk size significantly reduced the total number of chunks.
* Retrieval relevance was lower than with 500-character chunks.
* Final answer quality remained the same.
* Some questions requiring information from different sections had insufficient retrieved context.

---

## Experiment Comparison

| Metric                      | 500-Character Chunks | 1000-Character Chunks |
| --------------------------- | -------------------: | --------------------: |
| Total Chunks                |                  176 |                    76 |
| Retrieved Context Relevance |                  90% |                83.33% |
| Final Answer Quality        |               96.67% |                96.67% |

---

## Conclusion

In this experiment, the 500-character chunk size performed better in terms of retrieved context relevance, achieving 90% compared to 83.33% for 1000-character chunks. However, both chunk sizes achieved the same final answer quality of 96.67%.

This suggests that smaller chunks provided more focused retrieval, while larger chunks reduced the number of stored chunks without improving final answer quality. Therefore, for this specific PDF and evaluation setup, the 500-character chunk size produced better retrieval results, although the difference in retrieval quality did not affect the final answer quality.

Further experiments with different chunk sizes, overlap values, and `TOP_K` values are required before determining the optimal configuration for the RAG pipeline.
