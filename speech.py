import pyttsx3

class TTS:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text):
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print("An exception occurred during speech:", e)