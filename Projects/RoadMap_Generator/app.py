from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini API - Replace YOUR_GEMINI_API_KEY with your actual API key
genai.configure(api_key="API-KEY")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_roadmap():
    try:
        data = request.get_json()
        field = data.get('field', '')
        goal = data.get('goal', '')
        
        if not field or not goal:
            return jsonify({'error': 'Both field and goal are required'}), 400
        
        # Create the prompt for Gemini
        prompt = f"""Generate a detailed career roadmap for someone interested in {field}. Their career goal is: {goal}.

Please provide a structured roadmap with:
1. Current skills assessment
2. Short-term goals (3-6 months)
3. Medium-term goals (6-12 months)
4. Long-term goals (1-3 years)
5. Recommended learning resources
6. Key milestones and checkpoints
7. Potential challenges and how to overcome them

Format the response in a clear, actionable way that someone can follow step by step."""

        # Generate response from Gemini
        response = model.generate_content(prompt)
        
        return jsonify({
            'success': True,
            'roadmap': response.text,
            'field': field,
            'goal': goal
        })
        
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000) 
