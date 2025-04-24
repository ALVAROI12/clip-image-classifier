from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from transformers import CLIPProcessor, CLIPModel
from PIL import Image, UnidentifiedImageError
from io import BytesIO
import torch

# ✅ Create the FastAPI app
app = FastAPI()

# ✅ Allow requests from any origin (for Streamlit frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Load the CLIP model and processor once at startup
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# ✅ Define classification labels
labels = ["cat", "dog", "car", "plane", "tree", "book", "laptop", "shoe", "cup", "phone"]

# ✅ POST endpoint for image classification
@app.post("/classify")
async def classify_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        print(f"📦 File name: {file.filename}")
        print(f"📎 Content type: {file.content_type}")
        print(f"🧱 Byte size: {len(contents)}")

        image = Image.open(BytesIO(contents)).convert("RGB")

    except UnidentifiedImageError:
        return {"error": "Uploaded file is not a valid image. Please try a JPG or PNG."}
    except Exception as e:
        return {"error": f"Failed to process image: {str(e)}"}

    try:
        inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)
        outputs = model(**inputs)
        logits_per_image = outputs.logits_per_image
        probs = logits_per_image.softmax(dim=1).tolist()[0]

        return {label: round(float(prob), 4) for label, prob in zip(labels, probs)}

    except Exception as e:
        return {"error": f"Inference failed: {str(e)}"}
