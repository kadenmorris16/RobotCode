import speech
import openai
import random
import speech_recognition as sr

class ChatGPT:
    def __init__(self):
        self.client = openai.OpenAI(api_key="")
        self.engine = speech.TTS()

    def question_random(self, string):
        rand = random.randint(1,6)
        if(rand == 1):
            print("funny")
            return self.question_funny(string)
        elif(rand == 2):
            print("mean")
            return self.question_mean(string)
        elif(rand == 3):
            print("smart")
            return self.question_smart(string)
        elif(rand == 4):
            print("dumb")
            return self.question_dumb(string)
        elif(rand == 5):
            print("enthusiastic")
            return self.question_enthusiastic(string)
        elif(rand == 6):
            print("rhyme")
            return self.question_rhyme(string)

    def question_funny(self, string):
        try:
            response = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt="Answer in under 15 words with a joke that will make me laugh uncontrollably: " + string,
                max_tokens=25
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}", None
        
    def question_mean(self, string):
        try:
            response = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt="Respond in under 15 words with a cutting remark that would leave someone speechless: " + string,
                max_tokens=25
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}", None
        
    def question_smart(self, string):
        try:
            response = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt="Respond to me in under 15 words as if you're smarter than Einstein: " + string,
                max_tokens=25
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}", None
        
    def question_dumb(self, string):
        try:
            response = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt="Answer in under 15 words as if you are concussed: " + string,
                max_tokens=25
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}", None
        
    def question_enthusiastic(self, string):
        try:
            response = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt="Reply in under 15 words with boundless enthusiasm, as if you've just won the lottery: " + string,
                max_tokens=25
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}", None
        
    def question_rhyme(self, string):
        try:
            response = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt="Reply with a single rap line: " + string,
                max_tokens=25
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}", None

def robot_listen():
    ai = ChatGPT()
    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            r.energy_threshold = 300

            try:
                print("\nAsk a question!")
                audio = r.listen(source)
                text = r.recognize_google(audio)
                print("You said:", text)

                response = ai.question_random(text)
                print("Response:", response)
                ai.engine.speak(response)
            except sr.UnknownValueError:
                print("I don't understand...")

if __name__ == "__main__":
    robot_listen()