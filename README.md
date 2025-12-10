# SemEval Task 8 — Milvus-Based Dense Retrieval Pipeline
This repository contains our implementation for **SemEval 2025 Task 8 (MTRAGEval)**, 
focused on evaluating **multi-turn retrieval-augmented generation (RAG)** systems.  
Our approach implements a full dense-retrieval pipeline using **MiniLM**, **Contriever**, 
and **Milvus** to store and search dense passage embeddings over the **CLAPNQ** dataset.

---

## 🔍 Overview

We build a complete retrieval pipeline that performs:

1. **Embedding generation**  
2. **Vector storage in Milvus**  
3. **Approximate nearest neighbor (ANN) retrieval**  
4. **Prediction formatting** for SemEval Task 8  
5. **Evaluation** using the official `run_retrieval_eval.py` script  

Two embedding models were tested:

- **MiniLM (all-MiniLM-L6-v2)** → *primary working system*
- **Contriever** → *secondary experiment (partial due to hardware limits)*
