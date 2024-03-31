import speech
import openai
import random

class ChatGPT:
    def __init__(self):
        self.client = openai.OpenAI(api_key="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")
        self.engine = speech.TTS()

    def question_random(self, string):
        rand = random.randint(1,5)
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

    def question_funny(self, string):
        try:
            response = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt="Answer (in under 15 words) with a joke that will make me laugh uncontrollably: " + string,
                max_tokens=25
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}", None
        
    def question_mean(self, string):
        try:
            response = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt="Respond (in under 15 words) with a cutting remark that would leave someone speechless: " + string,
                max_tokens=25
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}", None
        
    def question_smart(self, string):
        try:
            response = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt="Answer (in under 15 words) by pretending you're smarter than Einstein: " + string,
                max_tokens=25
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}", None
        
    def question_dumb(self, string):
        try:
            response = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt="Give an answer (in under 15 words) that's so simple, even a child could understand it: " + string,
                max_tokens=25
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}", None
        
    def question_enthusiastic(self, string):
        try:
            response = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt="Reply (in under 15 words) with boundless enthusiasm, as if you've just won the lottery: " + string,
                max_tokens=25
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}", None

if __name__ == "__main__":
    ai = ChatGPT()
    q = "Where is the engineering building?"
    response= ai.question_random(q)
    print("Response:", response)
    ai.engine.speak(response)