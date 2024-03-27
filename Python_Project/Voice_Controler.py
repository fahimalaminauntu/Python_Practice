import speech_recognition as sr
import pyttsx3
import time

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"Recognized command: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def perform_action(command):
    if "hello" in command:
        print("Hello! How can I help you?")
        speak("Hello! How can I help you?")
    elif "what time is it" in command:
        print(f"The current time is {time.strftime('%I:%M %p')}")
        speak(f"The current time is {time.strftime('%I:%M %p')}")
    elif "goodbye" in command:
        print("Goodbye!")
        speak("Goodbye!")
    else:
        print("I'm not sure what you want me to do.")
        speak("I'm not sure what you want me to do.")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        command = listen_for_command()
        if command:
            perform_action(command)
            time.sleep(1)