# 🧠 CLIP-Based Image Classification API

A complete end-to-end image classification system using OpenAI's **CLIP** model, **FastAPI** for the backend, and **Streamlit** for the frontend.

Users can upload an image and get predictions for predefined categories. The backend is deployed on **Google Cloud Run**, and the frontend is hosted via **Streamlit Cloud**.

---

## 🚀 Live Demo

- **Backend API (Swagger UI):**  
  [https://clip-api-395534824176.us-central1.run.app/docs](https://clip-api-395534824176.us-central1.run.app/docs)

- **Frontend (Streamlit App):**  
  [https://clip-image-classifier-wjptsvvtwpfsk6hedijmay.streamlit.app/](https://clip-image-classifier-wjptsvvtwpfsk6hedijmay.streamlit.app/)

---

## ⚙️ How to Run It Locally

### 🔧 Backend (FastAPI + CLIP)

```bash
# Create and activate environment
conda create -n clip-backend python=3.10
conda activate clip-backend

# Install dependencies
pip install -r backend/requirements.txt

# Start the backend
cd backend
uvicorn main:app --reload

