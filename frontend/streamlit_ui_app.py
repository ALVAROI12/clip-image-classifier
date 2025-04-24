import streamlit as st
import requests
from PIL import Image

st.set_page_config(page_title="CLIP Image Classifier", layout="centered")
st.title("🧠 CLIP Image Classifier")
st.write("Upload an image to classify it using CLIP (deployed on Google Cloud Run).")

API_URL = "https://clip-api-395534824176.us-central1.run.app/classify"

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Classifying..."):
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        try:
            response = requests.post(API_URL, files=files)
            if response.status_code == 200:
                result = response.json()
                st.success("Classification Results")
                sorted_probs = sorted(result.items(), key=lambda x: x[1], reverse=True)
                for label, prob in sorted_probs:
                    st.write(f"**{label}**: {prob:.4f}")
            else:
                st.error(f"API call failed: {response.status_code}")
                st.code(response.text)
        except Exception as e:
            st.error("Error reaching the API.")
            st.code(str(e))
