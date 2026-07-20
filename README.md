
<h1 align="center">✨ NILA – AI Voice Assistant</h1>
 
  

<p align="center">
  A conversational AI voice assistant powered by OpenAI – built in Python 💻🎙️
  <br><br>
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/OpenAI-GPT3.5-informational?style=for-the-badge&logo=openai">
  <img src="https://img.shields.io/badge/SpeechRecognition-Enabled-success?style=for-the-badge">
</p>

---

## 📌 Overview

**NILA** is your AI-powered voice companion that:

- 🎧 Listens to your voice
- 🤖 Thinks using GPT-3.5
- 🗣️ Talks back using realistic speech
- 🌐 Responds to voice commands like “Open Google” or “Open YouTube”

A beginner-friendly AI assistant made entirely with **Python**.

---

## 📁 Folder Structure

```

nila-ai/
│
├── apikey.py       # Your OpenAI API key
├── nila.py         # Main assistant script
└── README.md       # This file

````

---

## 🔧 Requirements

Install the required libraries with pip:

```bash
pip install openai pyttsx3 SpeechRecognition flask flask-cors
```

To use microphone input:

* **Windows**:
  Get the PyAudio `.whl` file [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and run:

  ```bash
  pip install PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl
  ```

* **Mac/Linux**:

  ```bash
  brew install portaudio
  pip install pyaudio
  ```

---

## 🔐 Set Up OpenAI API Key

Create a file called `apikey.py` with the following content:

```python
# apikey.py
api_data = "your_openai_api_key_here"
```

> ⚠️ Keep your API key secret.

---

## 🚀 How to Run

Start the voice assistant:

```bash
python nila.py
``` 

Then just speak naturally. Try these:

* “Hi Nila”
* “Open YouTube”
* “What is photosynthesis?”
* “Bye” — to exit

---

## 💬 AI Personality

Conversation format:

```
Chando: Tell me about black holes.
NILA: Black holes are extremely dense points in space...
```

This prompt format makes the AI act like a friendly helper.

---
 
## 🌟 Features to Explore

✅ GPT-powered responses
✅ Speech-to-text and text-to-speech
✅ Voice commands (Google, YouTube)
✅ Easy customization for your own assistant
✅ Bengali language support (optional upgrade)

---

## 🧠 Demo

> 🎤 **You**: What is the capital of Japan?
> 💬 **NILA**: The capital of Japan is Tokyo.

---

## 🙌 Credits

Built with ❤️ using:

* [OpenAI API](https://platform.openai.com/)
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
* [pyttsx3](https://pypi.org/project/pyttsx3/)
* Python 3.10+

---

## 📄 License

Free to use and modify for educational and personal projects.

---

