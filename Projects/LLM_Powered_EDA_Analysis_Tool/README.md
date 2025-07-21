# 📊 LLM-Powered Exploratory Data Analysis (EDA) App

A powerful tool that performs automatic EDA (Exploratory Data Analysis) on any uploaded CSV file — with AI-generated insights powered by local LLMs using **Ollama** and an interactive UI built with **Gradio**.

---

## 🚀 Features

- ✅ Upload any `.csv` dataset
- 📈 Auto-generated histograms, boxplots & correlation heatmaps
- 🤖 AI-powered summary insights using **Mistral** via **Ollama**
- 📋 Clean missing values using median/mode logic
- 💻 Lightweight app — runs locally, no internet required
- 🌐 Launches with an easy-to-use Gradio web interface

---

## 📷 Demo

![demo](https://github.com/yourusername/llm-eda-app/assets/your-screenshot.gif)

---

## 🧠 How it Works

1. You upload a dataset
2. The app:
   - Cleans missing values
   - Creates summary statistics
   - Generates visualizations
   - Sends a summary to an LLM (Mistral via Ollama) to generate insights
3. You get:
   - A full EDA report
   - Gallery of plots
   - AI-generated human-like insights

---

## 🔧 Requirements

- Python 3.8+
- [Ollama](https://ollama.com) (installed & running)
- Python libraries:
  - `gradio`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `ollama`

Install them via:
```bash
pip install gradio pandas matplotlib seaborn ollama
