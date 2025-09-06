import streamlit as st
import numpy as np
from keras.models import load_model
from PIL import Image
from streamlit_drawable_canvas import st_canvas

# Load the trained ANN model
model = load_model("mnist_ann.h5")

st.set_page_config(page_title="MNIST Digit Classifier", page_icon="🖊️", layout="centered")
st.title("🖊️ Handwritten Digit Classifier")
st.write("Upload a 28x28 grayscale image of a digit (0-9) or draw it below:")

# Option to upload or draw
option = st.radio("Choose input method:", ("Upload Image", "Draw Digit"))

def preprocess_image(img):
    img = img.resize((28, 28))
    img_array = np.array(img).astype('float32') / 255.0
    img_array = img_array.reshape(1, 784)  # Flatten for ANN
    return img_array

if option == "Upload Image":
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        img = Image.open(uploaded_file).convert("L")
        st.image(img, caption="Uploaded Image", use_column_width=True)

        # Preprocess for ANN
        img_array = preprocess_image(img)

        # Prediction
        prediction = model.predict(img_array)
        pred_class = np.argmax(prediction)
        confidence = np.max(prediction) * 100

        st.subheader(f"Predicted Digit: {pred_class}")
        st.write(f"Confidence: {confidence:.2f}%")

else:
    # Drawing canvas
    canvas_result = st_canvas(
        fill_color="black",
        stroke_width=15,
        stroke_color="white",
        background_color="black",
        width=280,
        height=280,
        drawing_mode="freedraw",
        key="canvas",
    )
    
    if canvas_result.image_data is not None:
        img = Image.fromarray(np.uint8(canvas_result.image_data)).convert("L")
        img_array = preprocess_image(img)

        # Prediction
        prediction = model.predict(img_array)
        pred_class = np.argmax(prediction)
        confidence = np.max(prediction) * 100

        st.subheader(f"Predicted Digit: {pred_class}")
        st.write(f"Confidence: {confidence:.2f}%")
