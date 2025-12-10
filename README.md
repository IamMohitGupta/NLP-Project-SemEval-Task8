SemEval 2026 — Task 8 (MTRAGEval): Multi-Turn RAG System

This repository contains our implementation for SemEval 2026 Task 8, which evaluates multi-turn Retrieval-Augmented Generation (RAG) across:

Subtask A: Passage Retrieval

Subtask B: Grounded Generation (with gold passages)

Subtask C: Full RAG (retrieval + generation)

Our system uses dense retrieval, cross-encoder reranking, answerability detection, and local LLM generation to produce evidence-grounded responses.

🔍 Overview

We build a modular RAG pipeline that includes:

Dense Retrieval: MiniLM, Snowflake-Arctic embeddings with Milvus, pgvector, or FAISS

Reranking: bge-reranker-v2-m3 for fine-grained ranking improvements

Generation: Qwen2-1.5B-Instruct for grounded multi-turn responses

Answerability Check: Detects when retrieved evidence is insufficient

Memory Mechanism: Recent-turn buffer + optional long-term summary

Our experiments focus on the ClapNQ (Wikipedia) and Cloud corpora.


Evaluation scripts: https://github.com/IBM/mt-rag-benchmark/blob/main/scripts/evaluation/README.md
