# CLIP-Based Image Classification API

A complete end-to-end image classification system using OpenAI's CLIP model, FastAPI for the backend, and Streamlit for the frontend. The app allows users to upload an image and receive predictions for predefined categories. The backend is deployed on Google Cloud Run, and the frontend can be run locally or deployed via Streamlit Cloud.

🚀 Live Demo
Backend API: Cloud Run Endpoint

Frontend UI (if deployed): Coming soon via Streamlit Cloud or run locally below

⚙️ How to Run It Locally
🔧 Backend (FastAPI + CLIP)

Create a Conda or virtualenv environment:
conda create -n clip-backend python=3.10
conda activate clip-backend

install dependencies:
pip install -r backend/requirements.txt

Run the FastAPI server:
cd backend
uvicorn main:app --reload

Visit http://127.0.0.1:8000/docs to try the Swagger UI.

Frontend (Streamlit)
In the same environment, install Streamlit if not already:
pip install streamlit

Run the UI:
cd frontend
streamlit run streamlit_ui_app.py

Visit http://localhost:8501 to use the app.

☁️ Deployment
🔥 Backend on Google Cloud Run
Build Docker image:
gcloud builds submit --tag gcr.io/clip-image-classifier/clip-api

Deploy:
gcloud run deploy clip-api \
  --image gcr.io/clip-image-classifier/clip-api \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --memory=2Gi

(Optional) Deploy Frontend to Streamlit Cloud
Push this repo to GitHub

Go to streamlit.io/cloud

Create a new app:

Repo: ALVAROI12/clip-image-classifier

File: frontend/streamlit_ui_app.py

Deploy and get a public URL!

📊 Model Info
Model: openai/clip-vit-base-patch32

Framework: Hugging Face Transformers + PyTorch

Input: Uploaded image

Output: JSON with class probabilities

Labels Used: ["cat", "dog", "car", "plane", "tree", "book", "laptop", "shoe", "cup", "phone"]

eport & Documentation
IEEE-style report in /docs

Inference diagram: CLIP_inference_diagram.png

Demo link: demo_link.txt

Screenshots of API and UI included for presentation/report



## Features
- Upload images using `/classify` API
- Get predictions for labels like cat, dog, car, etc.
- Runs locally and can be deployed on Google App Engine

## How to Run Locally

```bash
conda activate clip-backend
uvicorn main:app --reload
