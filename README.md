Voice Calculator using Python

Overview:
This project is a simple Voice-Controlled Calculator built using Python. It listens to the user's spoken mathematical expression, converts it into a valid arithmetic expression, evaluates it, and then speaks out the result using text-to-speech.
It uses speech recognition to capture voice input and pyttsx3 for voice output.

Features:
Takes voice input from microphone
Converts spoken words into mathematical operators

Supports basic arithmetic operations:
Addition
Subtraction
Multiplication
Division
Power

Speaks out the final result
Handles errors gracefully

Technologies Used:
Python
speech_recognition
pyttsx3
Microphone input (PyAudio required)

Installation:
Install required libraries using pip:
pip install speechrecognitionpip install pyttsx3pip install pyaudio

If pyaudio gives error on Windows, install it using:
pip install pipwinpipwin install pyaudio

How to Run:
Connect a working microphone

Run the Python script:
python voice_calculator.py

Speak a math expression like:
"five plus three"
"ten divided by two"
"four multiplied by six"

The program will show result.


How It Works:
Captures voice input using speech_recognition
Converts speech to text using Google Speech API

Replaces words like "plus", "minus", "divide by" into symbols
Evaluates the expression using eval()
Speaks the result using pyttsx3

Notes:
Requires stable internet for speech recognition
Avoid complex or unclear speech inputs
eval() is used for simplicity (not recommended for secure production apps)


Developers:
Mahnoor Nadeem
Tazeem Fatima
