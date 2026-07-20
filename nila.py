import os
import webbrowser
import pyttsx3
import speech_recognition as sr
from openai import OpenAI
from apikey import get_api_key

try:
    import tkinter as tk
except Exception:
    tk = None

API_KEY = get_api_key()
client = OpenAI(api_key=API_KEY) if API_KEY else None


def detect_language(text):
    if any(ord(ch) > 127 for ch in text):
        return "bn" if any("া" <= ch <= "৺" or "অ" <= ch <= "৯" for ch in text) else "unknown"
    return "bn" if any(char in text.lower() for char in ["আ", "এই", "কি", "কেমন", "তুমি", "আমার", "আপনি"]) else "en"


def get_reply(question):
    if not API_KEY:
        return "OpenAI API key is not set. Please add your key to apikey.py or the OPENAI_API_KEY environment variable."

    try:
        assert client is not None
        lang = detect_language(question)
        system_prompt = "You are NILA, a friendly AI assistant." if lang == "en" else "তুমি NILA, একবারে বন্ধুত্বপূর্ণ এবং সহায়ক AI সহকারী."
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question},
            ],
            max_tokens=220,
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
        query = recognizer.recognize_google(audio, language="bn-IN" if detect_language(" ".join(["তুমি", "কেমন", "আছো"])) == "bn" else "en-in")
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


def run_cli():
    speak("Hello! I'm NILA, your personal AI assistant. How can I help you today?")

    while True:
        query = take_command()
        if not query:
            continue

        if "open youtube" in query or "ইউটিউব খুলো" in query:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")
        elif "open google" in query or "গুগল খুলো" in query:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")
        elif "bye" in query or "exit" in query or "quit" in query or "বিদায়" in query:
            speak("Goodbye! Have a great day.")
            break
        else:
            answer = get_reply(query)
            speak(answer)


if tk is not None:
    class NilaGUI:
        def __init__(self, root):
            self.root = root
            self.root.title("NILA Assistant")
            self.root.geometry("420x260")

            tk.Label(root, text="NILA", font=("Segoe UI", 16, "bold")).pack(pady=8)
            self.input_box = tk.Entry(root, width=40)
            self.input_box.pack(pady=6)
            self.output_box = tk.Text(root, height=10, width=48)
            self.output_box.pack(pady=6)
            tk.Button(root, text="Ask", command=self.ask).pack()

        def ask(self):
            question = self.input_box.get().strip()
            if not question:
                return
            self.output_box.delete("1.0", tk.END)
            self.output_box.insert(tk.END, "Thinking...\n")
            reply = get_reply(question)
            self.output_box.delete("1.0", tk.END)
            self.output_box.insert(tk.END, reply)
            speak(reply)


def launch_gui():
    if tk is None:
        print("Tkinter is not available in this environment.")
        return
    root = tk.Tk()
    app = NilaGUI(root)
    root.mainloop()


if __name__ == '__main__':
    run_cli()
