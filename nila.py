import os
import webbrowser
import pyttsx3
import speech_recognition as sr
from openai import OpenAI
from apikey import api_data

client = OpenAI(api_key=api_data or os.getenv("OPENAI_API_KEY"))


def get_reply(question):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are NILA, a friendly AI assistant."},
                {"role": "user", "content": question},
            ],
            max_tokens=200,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as exc:
        return f"Sorry, I couldn't reach the AI service right now. Error: {exc}"


def init_tts():
    try:
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty("voices")
        if voices:
            engine.setProperty("voice", voices[0].id)
        engine.setProperty("rate", 170)
        return engine
    except Exception:
        return None


engine = init_tts()


def speak(text):
    print(f"NILA: {text}")
    if engine is not None:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception:
            pass


def take_command():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1
    recognizer.energy_threshold = 300

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("🎤 Listening...")
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=8)

        print("🔎 Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"User: {query}\n")
        return query.lower()

    except sr.WaitTimeoutError:
        speak("I didn't hear anything. Please try again.")
        return None
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please try again.")
        return None
    except sr.RequestError as exc:
        print(f"Speech recognition service error: {exc}")
        speak("Voice recognition is unavailable right now. Please type your request.")
        return input("You: ").strip().lower() or None
    except OSError as exc:
        print(f"Microphone error: {exc}")
        speak("Microphone is not available. Please type your request.")
        return input("You: ").strip().lower() or None
    except Exception as exc:
        print(f"Voice input error: {exc}")
        speak("I'm switching to text input for now.")
        return input("You: ").strip().lower() or None


if __name__ == '__main__':
    speak("Hello! I'm NILA, your personal AI assistant. How can I help you today?")

    while True:
        query = take_command()
        if not query:
            continue

        if "open youtube" in query:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")
        elif "open google" in query:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")
        elif "bye" in query or "exit" in query or "quit" in query:
            speak("Goodbye! Have a great day.")
            break
        else:
            answer = get_reply(query)
            speak(answer)
