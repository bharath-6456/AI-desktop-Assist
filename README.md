AI Desktop Assistant

AI Desktop Assistant is a Python-based voice assistant designed to simplify tasks like launching applications, sending emails, and retrieving real-time weather updates. Integrated with Vosk for speech recognition and OpenAI's GPT API for handling queries, it serves as a hands-free productivity tool for your desktop.

Table of Contents
Features
Installation
Usage
Technologies
Project Structure
Future Improvements
Contributing
License
Features
Speech Recognition: Uses Vosk for offline voice recognition and converts commands to text.
Voice Response: Provides audible responses using the pyttsx3 text-to-speech engine.
Task Automation: Capable of launching applications, sending emails, and fetching real-time weather updates.
Conversational AI: Integrated with OpenAI's GPT API to answer user queries.
Modular Design: Easily extendable for adding more commands or functionalities.
Installation
Prerequisites
Python 3.8+
An API key from OpenAI for GPT integration
Steps
Clone the Repository

bash
Copy code
git clone https://github.com/bharath-6456/voice-assistant.git
cd voice-assistant
Install Dependencies

Use the following command to install required Python packages:

bash
Copy code
pip install -r requirements.txt
Setup API Keys

Obtain your OpenAI API key by registering at OpenAI.

Create a .env file in the root directory and add your API key:

plaintext
Copy code
OPENAI_API_KEY=your_openai_api_key
Download Vosk Model

Download the Vosk model for offline voice recognition from Vosk models.
Place the model in a models directory within the project and update the code path accordingly if needed.
Usage
To start the assistant, run:

bash
Copy code
python assistant.py
Commands
Open Applications: Say commands like "Open browser," "Launch Visual Studio Code," etc.
Check Weather: Say "What's the weather?" or "Tell me the weather in [City]."
Send Emails: Say "Send an email to [Contact Name]" and follow the prompts.
General Questions: Ask any question, and the assistant will use OpenAI's GPT API to respond.
Technologies
Speech Recognition: Vosk
Text-to-Speech: pyttsx3
Conversational AI: OpenAI GPT API
Environment Configuration: python-dotenv
