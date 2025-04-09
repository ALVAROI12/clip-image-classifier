from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import torch
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Lazy-load model and processor
model = None
processor = None

labels = ["cat", "dog", "car", "plane", "tree", "book", "laptop", "shoe", "cup", "phone"]

@app.on_event("startup")
async def load_model():
    global model, processor
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

@app.post("/classify")
async def classify_image(file: UploadFile = File(...)):
    global model, processor
    if model is None or processor is None:
        raise RuntimeError("Model not loaded")

    image = Image.open(io.BytesIO(await file.read())).convert("RGB")
    inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits_per_image, dim=1)[0]
    return {label: float(prob) for label, prob in zip(labels, probs)}
