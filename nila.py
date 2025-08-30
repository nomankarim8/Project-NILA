import openai
from apikey import api_data
import pyttsx3
import speech_recognition as sr
import webbrowser



# Initialize OpenAI
openai.api_key = api_data

# Function to get AI response
def get_reply(question):
    prompt = f"User: {question}\nNILA:"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use a newer, more capable model
        prompt=prompt,
        max_tokens=200,
        stop=["User:"]
    )
    
    answer = response.choices[0].text.strip()
    return answer

# Initialize Text-to-Speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use default voice

def speak(text):
    print(f"NILA: {text}")
    engine.say(text)
    engine.runAndWait()

# Welcome message
speak("Hello! I'm NILA, your personal AI assistant. How can I help you today?")

# Listen for voice input
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.pause_threshold = 1
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
