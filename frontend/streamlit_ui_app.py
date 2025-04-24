import streamlit as st
import requests
from PIL import Image

st.set_page_config(page_title="CLIP Image Classifier", layout="centered")
st.title("🧠 CLIP Image Classifier")
st.write("Upload an image to classify it using CLIP (local backend).")

API_URL = "https://clip-api-395534824176.us-central1.run.app/classify"

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        with st.spinner("Classifying..."):
            uploaded_file.seek(0)
            files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
            response = requests.post(API_URL, files=files)

            if response.status_code == 200:
                result = response.json()

                if "error" in result:
                    st.error("❌ API Error:")
                    st.code(result["error"])
                else:
                    st.success("✅ Top Prediction")
                    top_label, top_score = max(
                        {label: float(prob) for label, prob in result.items()}.items(),
                        key=lambda x: x[1]
                    )
                    st.markdown(f"🎯 **{top_label.capitalize()}** with **{top_score:.2%} confidence**")

            else:
                st.error("❌ Something went wrong.")
                st.code(response.text)

    except Exception as e:
        st.error("❌ Error processing the image.")
        st.code(str(e))
