import pyttsx3

text = "Hello World"
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()