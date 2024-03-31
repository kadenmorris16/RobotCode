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
                prompt="Answer with funny short phrase: " + string,
                max_tokens=25
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}", None
        
    def question_mean(self, string):
        try:
            response = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt="Answer with a short phrase in an angry tone: " + string,
                max_tokens=25
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}", None
        
    def question_smart(self, string):
        try:
            response = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt="Answer with a short phrase and pretend you're smarter than Einstein: " + string,
                max_tokens=25
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}", None
        
    def question_dumb(self, string):
        try:
            response = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt="Respond with a short phrase and improper grammar: " + string,
                max_tokens=25
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}", None
        
    def question_enthusiastic(self, string):
        try:
            response = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt="Respond with a short phrase like the happiest person in the world: " + string,
                max_tokens=25
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}", None

if __name__ == "__main__":
    ai = ChatGPT()
    q = "what is your best joke?"
    response= ai.question_random(q)
    print("Response:", response)
    ai.engine.speak(response)