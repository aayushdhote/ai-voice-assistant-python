print("✅ Assistant started...")

import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia

# Initialize the speech engine
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        talk("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        talk("Sorry, there's a problem with the service.")
        return ""

def run_assistant():
    command = listen()

    if "play" in command:
        song = command.replace("play", "")
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The current time is {time}")

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, sentences=1)
        talk(info)

    elif "stop" in command:
        talk("Goodbye!")
        exit()

    else:
        talk("Please say a command I can understand.")

# Run the assistant
while True:
    run_assistant()
