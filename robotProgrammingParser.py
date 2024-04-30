import time
import speech_recognition as sr
from speech import TTS
from gestures import Gesture
from speech import TTS
from tango import Tango
from screen import Screen

class RobotProgrammingParser():
    def __init__(self, actions, root):
        self.actions = actions
        self.tango = Tango()
        self.listen = sr.Recognizer()
        self.tts = TTS()
        self.gesture = Gesture(self.tango)
        self.display = Screen(root)

        self.display.drawEyes(5)
        self.gesture.start()
        self.run()

    def run(self):
        action_num = 1
        for action_str in self.actions:
            
            #self.display.printText("Action " + str(action_num) + "/" + str(len(self.actions)), 80)
            time.sleep(1)
            self.display.drawEyes(5)

            action = action_str.split()
            if action[0] == "Drive":
                self.completeDrive(action[1:])
            elif  action[0] == "Turn":
                self.completeTurn(action[1:])
            elif  action[0] == "HeadTilt":
                self.completeHeadTilt(action[1])
            elif  action[0] == "HeadTurn":
                self.completeHeadTurn(action[1])
            elif  action[0] == "WaistTurn":
                self.completeWaistTurn(action[1])
            elif  action[0] == "Listen":
                self.completeListen()
            elif  action[0] == "Talk":
                self.completeTalk(" ".join(action[1:]))
            else: #Gesture
                self.completeGesture(action[1])

            action_num += 1

        self.display.clear()

    def completeDrive(self, data): # data: 0=direction, 1=speed, 2=distance
        self.tango.setSpeed(0, int(data[1]))
        t = abs(30 - float(data[1])) * float(data[2]) / 5
        if(data[0] == "Forward"):
            self.tango.setServo(0, 5000)
        else:
            self.tango.setServo(0, 7000)
        time.sleep(t)
        self.tango.reset(0)

    def completeTurn(self, data): # data: 0=direction, 1=time
        self.tango.setSpeed(1, 20)
        if(data[0] == "Right"):
            self.tango.setServo(0, 5000)
        else:
            self.tango.setServo(0, 7000)
        time.sleep(float(data[1]))
        self.tango.reset(0)

    def completeHeadTilt(self, direction):
        if(direction == "Up"):
            self.gesture.headUp()
        else:
            self.gesture.headDown()

    def completeHeadTurn(self, direction):
        if(direction == "Left"):
            self.gesture.headLeft()
        else:
            self.gesture.headRight()

    def completeWaistTurn(self, direction):
        if(direction == "Left"):
            self.gesture.torsoLeft()
        else:
            self.gesture.torsoRight()

    def completeListen(self):
        while True:
            with sr.Microphone() as source:
                self.listen.adjust_for_ambient_noise(source)
                self.listen.energy_threshold = 300

                try:
                    print("\nListening...")
                    self.tts.speak("I'm Listening!")
                    audio = self.listen.listen(source)
                    text = self.listen.recognize_google(audio)
                    print("You said:", text)
                    self.tts.speak("You said... " + text)
                    break

                except sr.UnknownValueError:
                    print("I don't understand...")

    def completeTalk(self, string):
        self.tts.speak(string)

    def completeGesture(self, gesture):
        if gesture == "pointRight":
            self.gesture.pointRightSingle()
            time.sleep(1)
        elif  gesture ==  "pointLeft":
            self.gesture.pointLeftSingle()
            time.sleep(1)
        elif  gesture == "handsUp":
            self.gesture.armsUp()
            time.sleep(1)
        else:
            self.gesture.wave()

        self.gesture.start()