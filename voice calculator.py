~
import speech_recognition as sr
import pyttsx3
import tkinter as tk

# Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Convert spoken text into math
def convert_text_to_math(text):
    text = text.lower()

    replacements = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "ten": "10",
        "plus": "+",
        "minus": "-",
        "times": "*",
        "x": "*",
        "divide": "/"
    }

    for word, symbol in replacements.items():
        text = text.replace(word, symbol)

    return text

# Main voice function
def start_listening():
    with sr.Microphone() as source:
        status_label.config(text="Listening...")

        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            user_label.config(text=f"You said: {text}")

            expression = convert_text_to_math(text)

            result = eval(expression)

            result_label.config(text=f"Result: {result}")

            speak(f"The result is {result}")

        except Exception as e:
            result_label.config(text="Could not calculate")
            print(e)

# GUI Window
root = tk.Tk()
root.title("Voice Calculator")
root.geometry("400x300")

title_label = tk.Label(root, text="Voice Calculator", font=("Arial", 18))
title_label.pack(pady=10)

status_label = tk.Label(root, text="Press button and speak")
status_label.pack(pady=5)

user_label = tk.Label(root, text="")
user_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack(pady=20)

listen_button = tk.Button(root, text="Start Listening", command=start_listening)
listen_button.pack(pady=10)

root.mainloop()