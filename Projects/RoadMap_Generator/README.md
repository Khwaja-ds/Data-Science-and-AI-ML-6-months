# Career Roadmap Generator

A beautiful web application that generates personalized career roadmaps using AI. Built with Flask backend and vanilla HTML/CSS/JavaScript frontend.

## Features

✅ **Modern UI/UX**
- Beautiful gradient background
- Smooth animations and transitions
- Responsive design for all devices
- Loading animations during generation

✅ **Smart Career Guidance**
- AI-powered roadmap generation using Google Gemini
- Structured career planning with timelines
- Personalized recommendations based on field and goals

✅ **User-Friendly Interface**
- Clean, intuitive form design
- Copy to clipboard functionality
- Real-time notifications
- Keyboard shortcuts support

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd career-roadmap-generator
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Get Your Gemini API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the API key

### 4. Set Up Environment Variables
Create a `.env` file in the root directory:
```bash
# .env
GEMINI_API_KEY=your_actual_api_key_here
```

### 5. Run the Application
```bash
python app.py
```

The app will be available at: http://127.0.0.1:5000

## Usage

1. **Select Your Career Field**: Choose from the dropdown or select "Other" for custom fields
2. **Describe Your Goal**: Be specific about your career aspirations
3. **Generate Roadmap**: Click the button and wait for AI to create your personalized roadmap
4. **Copy & Share**: Use the copy button to save your roadmap

## Project Structure

```
career-roadmap-generator/
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── style.css         # CSS styles
│   └── script.js         # JavaScript functionality
└── README.md            # This file
```

## Features in Detail

### Frontend
- **HTML5**: Semantic markup with accessibility features
- **CSS3**: Modern styling with gradients, animations, and responsive design
- **JavaScript**: Vanilla JS with async/await for API calls
- **Font Awesome**: Icons for better visual experience
- **Google Fonts**: Inter font family for clean typography

### Backend
- **Flask**: Lightweight Python web framework
- **Google Gemini API**: AI-powered text generation
- **Environment Variables**: Secure API key management
- **JSON API**: RESTful endpoint for roadmap generation

### UI/UX Features
- **Loading States**: Visual feedback during API calls
- **Notifications**: Success/error messages with auto-dismiss
- **Copy to Clipboard**: One-click roadmap copying
- **Form Validation**: Real-time input validation
- **Keyboard Shortcuts**: Ctrl+Enter to submit, Escape to close notifications
- **Responsive Design**: Works on desktop, tablet, and mobile

## API Endpoints

### POST /generate
Generates a career roadmap based on user input.

**Request Body:**
```json
{
  "field": "AI/Artificial Intelligence",
  "goal": "Become a Senior AI Engineer at a tech company"
}
```

**Response:**
```json
{
  "success": true,
  "roadmap": "Detailed career roadmap text...",
  "field": "AI/Artificial Intelligence",
  "goal": "Become a Senior AI Engineer at a tech company"
}
```

## Customization

### Adding New Career Fields
Edit the select options in `templates/index.html`:
```html
<option value="Your New Field">Your New Field</option>
```

### Modifying the AI Prompt
Edit the prompt in `app.py` to change how the roadmap is generated:
```python
prompt = f"""Your custom prompt here..."""
```

### Styling Changes
Modify `static/style.css` to customize colors, fonts, and layout.

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your `.env` file is in the root directory and contains the correct API key
2. **Module Not Found**: Run `pip install -r requirements.txt` to install dependencies
3. **Port Already in Use**: Change the port in `app.py` or kill the process using the port

### Getting Help
- Check the browser console for JavaScript errors
- Check the Flask server logs for backend errors
- Ensure your Gemini API key is valid and has sufficient quota

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Credits

- Built with Flask and Google Gemini AI
- Icons by Font Awesome
- Fonts by Google Fonts
- Gradient backgrounds and modern UI design 