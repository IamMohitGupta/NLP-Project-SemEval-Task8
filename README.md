# SemEval 2026 — Task 8 (MTRAGEval): Multi-Turn Retrieval-Augmented Generation

This repository contains our unified implementation for **SemEval 2026 Task 8**, which evaluates multi-turn Retrieval-Augmented Generation (RAG) systems through three subtasks:  
**(A)** passage retrieval, **(B)** grounded generation with gold passages, and **(C)** full RAG generation.

Our work explores multiple retrieval, reranking, and generation strategies to understand how different components influence grounding quality in multi-turn conversational settings.

---

## ⭐ Summary of Our Approach

We build a complete RAG pipeline that covers all three subtasks with a combination of dense retrieval, reranking, answerability prediction, and grounded generation.

### 🔹 Retrieval (Subtask A)
We evaluate several retrieval backends and embedding models, including:

- **Dense Retrieval** with MiniLM and Snowflake-Arctic embeddings  
- **Vector Databases** such as Milvus, pgvector, and FAISS  
- **Diversity-Aware Retrieval** using Maximum Marginal Relevance (MMR)  
- **Cross-Encoder Reranking** with bge-reranker-v2-m3 for fine-grained semantic matching  

This allows us to compare lightweight CPU-friendly retrievers against larger and more expressive embedding models.

---

### 🔹 Grounded Generation (Subtask B)
For generation with gold passages, we use instruction-tuned local models such as **Qwen-1.5B**, incorporating:

- multi-turn conversation history  
- dataset-provided reference passages  
- grounding-focused instructions to minimize hallucination  

We additionally include an **answerability classifier** to detect when retrieved passages do not contain sufficient evidence.

---

### 🔹 Full RAG (Subtask C)
Subtask C integrates retrieval and generation into an end-to-end multi-turn RAG system:

1. Retrieve candidate passages  
2. Rerank with a cross-encoder  
3. Predict answerability  
4. Generate grounded answers  

A lightweight **memory mechanism** combines recent dialogue turns with a rolling summary to maintain context across long conversations.

---

## 📊 High-Level Findings

- **Cross-encoder reranking is crucial** for high recall and ranking accuracy on challenging datasets such as ClapNQ.  
- **Larger embedding models** (e.g., Snowflake-Arctic) deliver stronger retrieval performance, especially in technical domains.  
- **Model scale influences grounding** — Qwen-1.5B outperforms smaller models in factual consistency and answer quality.  
- **Gold passages alone do not guarantee better generation**, highlighting the importance of model reasoning ability.  
- Multi-turn RAG requires effective handling of conversational history and careful evidence selection.

---

## 📄 Reference

This project accompanies our paper:

**_MTRAGEval: Evaluating Multi-Turn RAG Conversations_**  
Mohit Gupta, Rayaan Lodhi, Yifan Tian  
(See project repository for PDF)
