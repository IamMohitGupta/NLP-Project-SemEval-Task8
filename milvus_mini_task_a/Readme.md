# Milvus + MiniLM Retrieval Pipeline (ClapNQ Dataset)

This project sets up a **vector retrieval system** using:

- **Milvus (Standalone)**
- **Attu UI Dashboard**
- **MiniLM (all-MiniLM-L6-v2)** embeddings
- **ClapNQ passage-level corpus** from the MTRAG benchmark

The goal is to build a retrieval pipeline for **SemEval 2026 Task 8 (Subtask A)**.

---

# 🚀 1. Start Milvus Using Docker

Milvus requires 3 services:
- milvus-standalone
- etcd
- minio

These are included in the official Milvus deployment repo.

### **Download the Milvus standalone docker-compose file**

```bash
wget https://github.com/milvus-io/milvus/releases/download/v2.6.5/milvus-standalone-docker-compose.yml -O docker-compose.yml
