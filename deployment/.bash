# Deploy to Google Cloud Run
gcloud auth configure-docker
docker build -t gcr.io/myproject/gen-ai-chatbot .
docker push gcr.io/myproject/gen-ai-chatbot
kubectl apply -f deployment/k8s-deploy.yaml