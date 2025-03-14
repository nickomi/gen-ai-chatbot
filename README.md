# AI Chatbot with Fine-Tuned LLM & RAG

A **fully production-ready AI chatbot** that combines **fine-tuned GPT-4 (LoRA) and Retrieval-Augmented Generation (RAG)** for contextual, high-quality responses.  

## Features  
**Fine-tuned GPT-4 with LoRA** (Hugging Face, PyTorch, PEFT)  
**Retrieval-Augmented Generation (RAG) using FAISS & Vector DB**  
**FastAPI REST API + WebSockets for real-time streaming**  
**Scalable deployment (Docker, Kubernetes, AWS/GCP)**  
**Frontend UI (Next.js + React for chatbot UI)**  
**CI/CD automation (GitHub Actions, Terraform, Helm Charts)**  

---

## **1. Setup & Installation**  

### **Prerequisites**  
- Python 3.9+  
- Node.js (for frontend)  
- Docker & Kubernetes (for deployment)  
- Google Cloud SDK or AWS CLI  

### **Clone the Repository**  
```bash
git clone https://github.com/your-username/gen_ai_chatbot.git
cd gen_ai_chatbot
```

### **Backend Installation (Fine-Tuning & API)**  
```bash
cd fine_tuning
pip install -r requirements.txt
python train_lora.py  # Fine-tunes GPT-4 with LoRA
```
```bash
cd ../api
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

### **Frontend Installation (React + Next.js)**  
```bash
cd ../frontend
npm install
npm run dev  # Starts the chatbot UI
```

---

## **2. Using the Chatbot**
### **Interact via API**
```bash
curl "http://localhost:8000/chat?query=Hello!"
```
### **Interact via Web UI**
Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## **3. Deployment (Docker + Kubernetes + CI/CD)**  

### **Docker Build & Run**
```bash
docker build -t ai-chatbot .
docker run -p 8000:8000 ai-chatbot
```

### **Deploy to Kubernetes**
```bash
kubectl apply -f deployment/k8s-deploy.yaml
kubectl get pods  # Check running pods
```

### **Deploy to Google Cloud Run**
```bash
gcloud builds submit --tag gcr.io/myproject/gen-ai-chatbot
gcloud run deploy chatbot --image gcr.io/myproject/gen-ai-chatbot --platform managed
```

### **CI/CD Pipeline (GitHub Actions)**
Every push to `main` automatically triggers a deployment:
```yaml
name: Deploy AI Chatbot

on: [push]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repo
        uses: actions/checkout@v2

      - name: Deploy to GCP
        run: |
          gcloud auth activate-service-account --key-file=gcp-key.json
          gcloud run deploy chatbot --image=gcr.io/myproject/gen-ai-chatbot --region=us-central1
```

---
