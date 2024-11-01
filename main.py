import datetime
import json
import os
import queue
import webbrowser
#import google.generativeai as genai
import openai
import pyttsx3
import sounddevice as sd
import smtplib
import requests
from vosk import Model, KaldiRecognizer
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Queue to hold audio data
q = queue.Queue()

# Callback function to capture audio input
def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

# Ensure that the model path is correct
model_path = r"C:\Users\lenovo thinkbook\PycharmProjects\pythonProject2\vosk-model-small-en-us-0.15\vosk-model-small-en-us-0.15"
model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

# Function to listen for voice input
def listen():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Listening...")
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                print("You said:", result['text'])
                return result['text'].lower()  # Convert to lowercase for consistent command handling

# Function to convert text to speech
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to ask a question to OpenAI's GPT model using the latest API
# def ask_ai(question):
#     genai.configure("AIzaSyAb-Z4Dt5Mr0yQ0p5Py_iX8PfALK3onDQA")
#
#     model = genai.GenerativeModel('gemini-1.5-flash')
#     response = model.generate_content(question)
#
#     # openai.api_key = "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"  # Replace with your OpenAI API key
#     # response = openai.chat.completions.create(
#     #     model="gpt-4o-mini",  # You can switch to "gpt-4" if you have access
#     #     messages=[
#     #         {"role": "system", "content": "You are a helpful assistant."},
#     #         {"role": "user", "content": question}
#     #     ]
#     # )
#     answer = response['choices'][0]['message']['content'].strip()
#     return answer

# Function to get weather updates
def get_weather(city):
    api_key = "e9ac9860f40e984df6654a801c9cbf35"  # Replace with your OpenWeather API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        main = weather_data["main"]
        wind = weather_data["wind"]
        weather_desc = weather_data["weather"][0]["description"]

        temperature = main["temp"]
        humidity = main["humidity"]
        wind_speed = wind["speed"]

        weather_report = (f"Temperature: {temperature}°C\n"
                          f"Humidity: {humidity}%\n"
                          f"Wind Speed: {wind_speed} m/s\n"
                          f"Weather Description: {weather_desc}")
    else:
        weather_report = "City Not Found"
    return weather_report

# Function to send an email
def send_email(recipient, subject, body):
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"  # Use app password for Gmail if 2FA is enabled

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient, text)
        server.quit()
        return "Email sent successfully."
    except Exception as e:
        return f"Failed to send email: {str(e)}"

if __name__ == "__main__":
    path = r"C:\Users\lenovo thinkbook\Downloads\chasing-horizons-228832.mp3"

    while True:
        text = listen()
        if "open google" in text:
            webbrowser.open("https://google.com")
            say("Opening Google")
        elif "open music" in text:
            os.startfile(path)
            say("Playing music")
        elif "the time" in text:
            curhr = datetime.datetime.now().strftime("%H")
            curmin = datetime.datetime.now().strftime("%M")
            say(f"Sir, the time is {curhr} hours and {curmin} minutes")
        elif "play" in text:
            say("Which city?")
            city = listen()
            weather = get_weather(city)
            say(f"The weather in {city} is as follows:\n{weather}")
        elif "send email" in text:
            say("Please provide the recipient email address.")
            recipient = listen()
            say("What is the subject?")
            subject = listen()
            say("What would you like to say?")
            body = listen()
            email_status = send_email(recipient, subject, body)
            say(email_status)
        elif "ask alexa" in text:
            say("What would you like to ask?")
            question = listen()
            answer = ask_ai(question)
            say(answer)
        elif "exit" in text or "stop" in text:
            say("Goodbye!")
            break
        else:
            say("Sorry, I didn't understand that command.")
