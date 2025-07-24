import os
from dotenv import load_dotenv
import streamlit as st
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit page config
st.set_page_config(
    page_title="🧠 Image to Text with Gemini",
    page_icon="🖼️",
    layout="wide"
)

# App UI
st.title("🖼️ Image to Text Generator using Gemini 1.5")
st.markdown("Turn any image into descriptive text using **Google Gemini 1.5 Flash**.")

# File uploader
uploaded_file = st.file_uploader("Upload an image (jpg/jpeg/png)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    col1, col2 = st.columns([1, 1])

    with col1:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

    with col2:
        with st.spinner("Analyzing image using Gemini 1.5..."):

            # Save to temporary file
            temp_file_path = "temp_image.jpg"
            image.save(temp_file_path)

            # Upload image file to Gemini
            uploaded_image = genai.upload_file(temp_file_path)

            # Initialize Gemini 1.5 Flash
            model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

            # Generate description
            response = model.generate_content([
                uploaded_image,
                "Please describe this image in detail."
            ])
            output_text = response.text

        st.subheader("🧠 AI Generated Description")
        st.markdown(output_text)
        st.download_button("📥 Download Text", data=output_text, file_name="output.txt")

        st.success("✅ Done! AI successfully generated text.")

# Footer
st.markdown("---")
st.markdown("💡 Built with [Gemini 1.5 Flash](https://ai.google.dev/) and Streamlit")
