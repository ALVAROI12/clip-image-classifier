# CLIP-Based Image Classification API

This project uses Hugging Face's CLIP model to classify images based on a set of predefined labels via a FastAPI backend.

## Features
- Upload images using `/classify` API
- Get predictions for labels like cat, dog, car, etc.
- Runs locally and can be deployed on Google App Engine

## How to Run Locally

```bash
conda activate clip-backend
uvicorn main:app --reload
