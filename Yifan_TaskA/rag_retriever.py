import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer


class FaissRetriever:
    def __init__(self, index_path="faiss_index.bin", metadata_path="passages.jsonl", model_name="sentence-transformers/all-MiniLM-L6-v2", top_k=5):
        self.index = faiss.read_index(index_path)
        self.metadata = [json.loads(line) for line in open(metadata_path)]
        self.model = SentenceTransformer(model_name)
        self.top_k = top_k

    def retrieve(self, query_text):
        # embed
        query_emb = self.model.encode([query_text], convert_to_numpy=True)
        faiss.normalize_L2(query_emb)

        # search
        D, I = self.index.search(query_emb, self.top_k)

        docs = []
        for idx in I[0]:
            docs.append(self.metadata[idx]["text"])

        return docs
