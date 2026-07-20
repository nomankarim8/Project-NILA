import os
import openai
from apikey import api_data
import pyttsx3
import speech_recognition as sr
import webbrowser

# Initialize OpenAI API key from environment or apikey.py
openai.api_key = api_data or os.getenv("OPENAI_API_KEY")

# Function to get AI response
def get_reply(question):
    messages = [
        {"role": "system", "content": "You are NILA, a friendly AI assistant."},
        {"role": "user", "content": question}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=200,
        temperature=0.7
    )

    return response.choices[0].message["content"].strip()

# Initialize Text-to-Speech
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(text):
    print(f"NILA: {text}")
    engine.say(text)
    engine.runAndWait()

# Listen for voice input
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("🎤 Listening...")
        audio = recognizer.listen(source)

    try:
        print("🔎 Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")
    except Exception:
        speak("Sorry, I didn't catch that. Please try again.")
        return None

    return query.lower()

# Main loop
if __name__ == '__main__':
    speak("Hello! I'm NILA, your personal AI assistant. How can I help you today?")

    while True:
        query = take_command()
        if not query:
            continue

        # Basic command handling
        if 'open youtube' in query:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")
        elif 'bye' in query or 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a great day.")
            break
        else:
            answer = get_reply(query)
            speak(answer)
