
# 🖼️ Image to Text Generator with Google Gemini

Turn any image into insightful text using Google Gemini 1.5 Flash and Streamlit. Just upload an image and let AI describe it intelligently.



---

## 🚀 Features

- 🧠 Describes any uploaded image using Gemini 1.5 Flash
- 📄 Download the generated text as a `.txt` file
- 🎨 Clean and responsive UI using Streamlit
- 🔐 API key protected using `.env`

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Google Generative AI (Gemini 1.5)**
- **Pillow (PIL)**
- **dotenv**

---

## 📁 Project Structure

```
image_to_text/
│
├── app.py                  # Main Streamlit app
├── .env                    # Environment variable with Gemini API key
├── requirements.txt        # All dependencies
└── README.md               # This file
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-username/image-to-text-gemini.git
cd image-to-text-gemini
```

2. **Create virtual environment (optional but recommended)**

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Add your Gemini API Key**

Create a `.env` file in the root directory and paste:

```env
GOOGLE_API_KEY=your_api_key_here
```

> 🔑 Get your API key from: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

5. **Run the app**

```bash
streamlit run app.py
```

---

## 📝 Example Use Cases

- Analyze complex images with descriptive output
- Generate image-based captions for content creation
- Educational tools for visually impaired users
- Automate documentation or labeling of visual content

---

## 📦 Dependencies

```
streamlit
Pillow
python-dotenv
google-generativeai
```

---

## 📜 License

MIT License — feel free to use, share, and improve!

---

## 🙌 Acknowledgments

- Built with [Google Generative AI](https://ai.google.dev/)
- Interface powered by [Streamlit](https://streamlit.io)


