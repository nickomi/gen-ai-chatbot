import faiss
import numpy as np
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def embed_text(texts):
    embeddings = [tokenizer.encode(text, add_special_tokens=True) for text in texts]
    embeddings = np.array([np.pad(e, (0, 512 - len(e))) for e in embeddings])
    return embeddings.astype(np.float32)

def create_faiss_index(docs):
    index = faiss.IndexFlatL2(512)
    vectors = embed_text(docs)
    index.add(vectors)
    return index

documents = ["Document 1", "Document 2"]
index = create_faiss_index(documents)
faiss.write_index(index, "rag_index.faiss")