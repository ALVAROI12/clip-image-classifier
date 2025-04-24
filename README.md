🧠 CLIP-Based Image Classification API
A complete end-to-end image classification system using OpenAI's CLIP model, FastAPI for the backend, and Streamlit for the frontend.

Users can upload an image and get predictions for predefined categories. The backend is deployed on Google Cloud Run, and the frontend is hosted via Streamlit Cloud.

🚀 Live Demo
Backend API (Swagger UI): https://clip-api-395534824176.us-central1.run.app/docs

Frontend (Streamlit App): https://clip-image-classifier-wjptsvvtwpfsk6hedijmay.streamlit.app/

⚙️ How to Run It Locally
Backend (FastAPI + CLIP)
Create and activate environment: conda create -n clip-backend python=3.10
conda activate clip-backend

Install dependencies:
pip install -r backend/requirements.txt

Run the backend:
cd backend
uvicorn main:app --reload

Open your browser and go to:
http://127.0.0.1:8000/docs

Frontend (Streamlit)
In the same environment, install Streamlit:
pip install streamlit

Run the UI:
cd frontend
streamlit run streamlit_ui_app.py

Open your browser and go to:
http://localhost:8501

☁️ Deployment
Backend on Google Cloud Run
Build Docker image:
gcloud builds submit --tag gcr.io/clip-image-classifier/clip-api

Deploy to Cloud Run:
gcloud run deploy clip-api --image gcr.io/clip-image-classifier/clip-api --platform managed --region us-central1 --allow-unauthenticated --memory=2Gi

Frontend on Streamlit Cloud
Push this repo to GitHub

Go to https://streamlit.io/cloud

Create a new app:
Repo: ALVAROI12/clip-image-classifier
File: frontend/streamlit_ui_app.py

Click Deploy and get a public URL

📊 Model Info
Model: openai/clip-vit-base-patch32

Framework: Hugging Face Transformers + PyTorch

Input: Uploaded image

Output: JSON with class probabilities

Labels: ["cat", "dog", "car", "plane", "tree", "book", "laptop", "shoe", "cup", "phone"]

📄 Report & Documentation
IEEE-style report: docs/IEEE_Final_Report_Template.docx

Inference diagram: docs/CLIP_inference_diagram.png

Demo link: docs/demo_link.txt

Screenshots: screenshots/

✨ Features
Upload images and classify them instantly

Get top predictions using CLIP model

Live backend and frontend with minimal setup

Easy to run locally or deploy to the cloud

👥 Team Contributions
Alvaro: Backend, Cloud Run Deployment, Coordination

Adam: CLIP Model Integration, Methodology Writing

Abhisek: Frontend UI, Testing, Results Writing

💬 Questions?
Open a GitHub issue or pull request to contribute.
Let’s build smart tools with AI!


