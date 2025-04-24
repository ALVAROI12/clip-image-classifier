# 🧠 CLIP-Based Image Classification API

A complete end-to-end image classification system using OpenAI's CLIP model, **FastAPI** for the backend, and **Streamlit** for the frontend.

Users can upload an image and receive predictions for predefined categories. The backend is deployed on **Google Cloud Run**, and the frontend is hosted via **Streamlit Cloud**.

---

## 🚀 Live Demo

- **Backend API (Swagger UI):**  
  [https://clip-api-395534824176.us-central1.run.app/docs](https://clip-api-395534824176.us-central1.run.app/docs)

- **Frontend (Streamlit App):**  
  [https://clip-image-classifier-wjptsvvtwpfsk6hedijmay.streamlit.app/](https://clip-image-classifier-wjptsvvtwpfsk6hedijmay.streamlit.app/)

---

## ⚙️ How to Run Locally

### 🔧 Backend (FastAPI + CLIP)

```bash
# Create and activate environment
conda create -n clip-backend python=3.10
conda activate clip-backend

# Install dependencies
pip install -r backend/requirements.txt

# Run the FastAPI server
cd backend
uvicorn main:app --reload

# Install Streamlit
pip install streamlit

# Run the UI
cd frontend
streamlit run streamlit_ui_app.py

# Build Docker image
gcloud builds submit --tag gcr.io/clip-image-classifier/clip-api

# Deploy to Cloud Run
gcloud run deploy clip-api \
  --image gcr.io/clip-image-classifier/clip-api \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --memory=2Gi


