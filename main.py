"""
🧠 Skills & Concepts You’ll Need to Learn
🎤 Voice Recognition	Use speech_recognition to convert speech to text	Real Python: Speech Recognition Guide
🗣 Text-to-Speech (TTS)	Use pyttsx3 or gTTS to speak responses	pyttsx3 Docs
🌍 API Integration	Fetch info from APIs like weather, quotes, Quran	Free APIs Collection
🧠 Command Routing	Turn phrases like "what's the time?" into code	Practice with if, match, or NLP libraries
💻 App Launcher	Use os or subprocess to open programs or files	subprocess module docs

🔧 Tech Stack

Python

Libraries:
    speech_recognition (voice input)

    pyttsx3 or gTTS (voice output)

    requests (APIs)

    datetime, os, subprocess, maybe re or nltk
"""
import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()
            
            print(f"Recognized {text}")

    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        continue

