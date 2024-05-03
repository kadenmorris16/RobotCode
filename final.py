import pyttsx3
from tango import Tango
import tkinter as tk
import time
import proj5_dialogue_engine as p5
import proj9 as p9
from screen import Screen
from threading import Thread

from gestures import Gesture

engine = pyttsx3.init()
root = tk.Tk()
display = Screen(root)
tango = Tango()
gesture = Gesture(tango)
gesture.start()
THRESHOLD = 100

def main():
    # Robot starts in quadrant A0 facing a random direction
    # Robot waits until it senses someone, then says a greeting from the dialogue script
    
    goto = 0 # Will be replaced by the quadrant the human asks to go to 
    if(p9.getDistance() < THRESHOLD):
        goto = p5.final(display)
    else:
        while(p9.getDistance() > THRESHOLD):
            print("No person detected")
            time.sleep(1)
        goto = p5.final(display)

    display.drawEyes(5)
    
    # Once the human asks to go to a quadrant, the robot takes them to the quadrant (try to be in the center)
    distances = p9.getSerialData()
    time.sleep(1)
    p9.moveForward()
    p9.determineAngle(distances, p9.getSerialData(), goto)
    p9.move(2)
    time.sleep(1)

    # Robot announces that it needs to charge the battery, then moves to the charging quadrant (A1) and announces "Charging activated"
    if(goto == 2):
        p9.turn(2, 'r')
    else:
        p9.turn(3, 'r')
    p9.move(3)
    engine.say("charging activated")
    engine.runAndWait()

Thread(target=main).start()
display.root.mainloop()