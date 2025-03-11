# Gemini Chatbot using Streamlit

This repository contains a simple chatbot application built using Streamlit and Google's Gemini API. The chatbot interacts with users in real-time and provides responses using the Gemini-2.0-flash model.

## Features
- Uses Google's Gemini-2.0-flash model for generating responses.
- Implements session-based chat history to track user interactions.
- Simple and interactive UI using Streamlit.
- Supports real-time question-answering with streaming responses.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/gemini-chatbot.git
   cd gemini-chatbot
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Setup Environment Variables
1. Create a `.env` file in the root directory and add your Google API key:
   ```sh
   GOOGLE_API_KEY=your_api_key_here
   ```

2. Load the environment variables in the script using `dotenv`.

## Usage
Run the Streamlit application:
```sh
streamlit run app.py
```

## File Structure
```
|-- app.py                # Main script for the chatbot
|-- requirements.txt      # List of required dependencies
|-- .env.example          # Example environment file
|-- README.md             # Project documentation
```

## Dependencies
- `streamlit`
- `google-generativeai`
- `python-dotenv`

## Contributing
Feel free to submit pull requests for improvements or bug fixes.
