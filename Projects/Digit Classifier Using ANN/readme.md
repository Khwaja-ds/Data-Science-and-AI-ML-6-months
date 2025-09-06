## 📊 How I Built the ANN Model  

I built this project using a simple **Artificial Neural Network (ANN)** instead of a CNN.  
Here’s the step-by-step explanation of how the model was created:  

### 1. Dataset  
- The **MNIST dataset** was used, which contains **70,000 images of handwritten digits (0–9)**.  
- Each image is **28x28 pixels** in grayscale.  
- The dataset is split into:
  - 60,000 images for training  
  - 10,000 images for testing  

### 2. Data Preprocessing  
- **Normalization**: Pixel values (0–255) were scaled down to the range **0–1** for faster training.  
- **Flattening**: Each 28x28 image was reshaped into a **1D vector of size 784** so it could be passed into a fully connected neural network.  
- **One-Hot Encoding**: Labels (0–9) were converted into categorical format, e.g., digit "3" → `[0,0,0,1,0,0,0,0,0,0]`.  

### 3. ANN Architecture  
The model was built using **Keras Sequential API** with the following layers:  

- **Input Layer**: 784 neurons (one for each pixel).  
- **Hidden Layer 1**: 128 neurons, ReLU activation.  
- **Hidden Layer 2**: 64 neurons, ReLU activation.  
- **Output Layer**: 10 neurons (for digits 0–9), Softmax activation.  

👉 ReLU was chosen for hidden layers because it helps avoid the vanishing gradient problem and speeds up training.  
👉 Softmax was chosen in the output layer to give a probability distribution across all 10 digit classes.  

### 4. Training  
- **Optimizer**: Adam (efficient gradient descent optimization).  
- **Loss Function**: Categorical Crossentropy (suitable for multi-class classification).  
- **Metrics**: Accuracy was used to evaluate performance.  
- **Epochs**: Trained for 10 iterations over the dataset with a batch size of 32.  

### 5. Saving the Model  
- After training, the model was saved in HDF5 format (`mnist_ann.h5`).  
- This allows the model to be loaded later in the Streamlit frontend for predictions.  

---

## 🎨 How I Built the Frontend  

The frontend was built using **Streamlit**, which makes it easy to deploy ML models with interactive UI.  

### 1. Input Options  
The app provides two ways to input a digit:  
- **Upload an Image**: Users can upload a pre-drawn digit image (28x28 grayscale).  
- **Draw a Digit**: Users can directly draw a digit on a canvas using the `streamlit-drawable-canvas` library.  

### 2. Preprocessing in Frontend  
- If an image is uploaded, it is resized to 28x28 and converted to grayscale.  
- If a digit is drawn, the canvas result is converted into a grayscale PIL image.  
- The processed image is then normalized (0–1), flattened into a vector of 784 values, and reshaped into the format required by the ANN.  

### 3. Prediction Workflow  
- The preprocessed image is passed to the loaded model (`mnist_ann.h5`).  
- The model outputs probabilities for each digit class (0–9).  
- The digit with the highest probability is selected as the **prediction**.  
- The app also shows the **confidence score (%)** of the prediction.  

### 4. UI/UX Features  
- A **radio button** lets users choose between Upload and Draw modes.  
- The predicted digit and confidence score are displayed dynamically.  
- Simple and clean layout designed with `st.set_page_config()` for better user experience.  

---

## ✅ Summary  
- The **ANN model** was built from scratch using only fully connected layers.  
- The model was trained on MNIST and saved as `mnist_ann.h5`.  
- The **frontend** was created with Streamlit, supporting both image uploads and digit drawing.  
- Users get real-time predictions with confidence scores in an interactive UI.  
