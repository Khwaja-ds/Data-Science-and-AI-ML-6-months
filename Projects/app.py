import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ollama
import os

# Function to Perform EDA and Generate Visualizations
def eda_analysis(file_path):
    try:
        df = pd.read_csv(file_path)
        
        # Fill missing values
        for col in df.select_dtypes(include=['number']).columns:
            df[col].fillna(df[col].median(), inplace=True)
        for col in df.select_dtypes(include=['object']).columns:
            df[col].fillna(df[col].mode()[0], inplace=True)
        
        # Summary
        summary = df.describe(include='all').to_string()
        missing_values = df.isnull().sum().to_string()
        
        # AI Insights
        insights = generate_ai_insights(summary)

        # Visualizations
        plot_paths = generate_visualizations(df)
        
        report = f"""
✅ Data Loaded Successfully!

📋 Summary:
{summary}

❓ Missing Values:
{missing_values}

🧠 AI Insights:
{insights}
"""
        return report, plot_paths
    
    except Exception as e:
        return f"❌ Error: {str(e)}", []

# AI-Powered Insights using Ollama (Mistral)
def generate_ai_insights(df_summary):
    prompt = f"Analyze the dataset summary and provide detailed insights:\n\n{df_summary}"
    try:
        response = ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"AI analysis failed: {e}"

# Generate Plots
def generate_visualizations(df):
    plot_paths = []
    os.makedirs("plots", exist_ok=True)

    for col in df.select_dtypes(include=['number']).columns:
        # Histogram
        plt.figure(figsize=(6,4))
        sns.histplot(df[col], bins=30, kde=True, color="skyblue")
        plt.title(f"Distribution of {col}")
        plt.tight_layout()
        path = f"plots/{col}_hist.png"
        plt.savefig(path)
        plot_paths.append(path)
        plt.close()

        # Boxplot
        plt.figure(figsize=(6,4))
        sns.boxplot(x=df[col], color='orange')
        plt.title(f"Boxplot of {col}")
        plt.tight_layout()
        path = f"plots/{col}_boxplot.png"
        plt.savefig(path)
        plot_paths.append(path)
        plt.close()
    
    # Correlation Heatmap
    numeric_df = df.select_dtypes(include=['number'])
    if not numeric_df.empty:
        plt.figure(figsize=(8,6))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        path = "plots/correlation_heatmap.png"
        plt.savefig(path)
        plot_paths.append(path)
        plt.close()

    return plot_paths

# Gradio Interface
demo = gr.Interface(
    fn=eda_analysis,
    inputs=gr.File(type="filepath"),
    outputs=[
        gr.Textbox(label="📊 EDA Report"),
        gr.Gallery(label="📈 Visualizations")
    ],
    title="📊 LLM-Powered Exploratory Data Analysis (EDA)",
    description="Upload any CSV file to get auto-generated summary, insights from Mistral (via Ollama), and visualizations."
)

demo.launch(share=True)
