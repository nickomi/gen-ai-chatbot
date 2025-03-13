from fastapi import FastAPI, Query
from transformers import AutoModelForCausalLM, AutoTokenizer
import faiss
import numpy as np

app = FastAPI()

# Load Model & Tokenizer
model = AutoModelForCausalLM.from_pretrained("fine_tuned_lora_model")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

# Load FAISS Index
index = faiss.read_index("rag_index.faiss")

def search_rag(query):
    vector = np.array([tokenizer.encode(query, add_special_tokens=True)])
    _, idxs = index.search(vector.astype(np.float32), k=1)
    return idxs

@app.get("/chat")
def chat(query: str = Query(..., description="User input query")):
    context = search_rag(query)
    input_text = f"Context: {context} Query: {query}"
    inputs = tokenizer(input_text, return_tensors="pt")
    response = model.generate(**inputs)
    return {"response": tokenizer.decode(response[0], skip_special_tokens=True)}
