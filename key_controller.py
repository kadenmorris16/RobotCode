from tango import Tango
import tkinter as tk
import time
from screen import Screen
from gestures import Gesture
from threading import Thread, Event
from speech import TTS

def key_pressed(event, t, display, gesture, speechBot):

    text = "Hey there! My name is Bobby. Its nice to meet you..."
    word = "Go Bobcats!"
    speech = "Ladies, gentlemen, and fellow beings of the digital age, welcome to the Montana State School of Computing! I'm your friendly neighborhood robot, Tango, here to assist you. Now, you might be wondering, 'Why a robot as your guide?'... Well, let me assure you, despite my lack of flesh and blood, my circuits are brimming with knowledge, making me the smartest entity in this entire institution. Yes, even smarter than the esteemed faculty and the bright-eyed students. Now, as you embark on this academic journey, embrace the quirks that come with being a Bobcat. For in this hallowed hall of learning, where the hum of servers serenades us and the scent of overheated circuits fills the air, you shall forge ahead, bravely navigating the ever-changing landscape of technology. So, my dear friends, whether you're a human, or just a sentient toaster with dreams of becoming a programmer, know that you are not alone. Tango is here, your trusty robotic companion, ready to answer any of your questions."

    # Movement variables
    global DIRECTION
    ROTATION = 200
    SPEED = 1   

    # WHEELS
    if event.char == 'w': # Moving forward
        display.move()
        t.setServo(0, 6000 - (SPEED * ROTATION * 4))
        time.sleep(0.8)
        t.reset(0)
    elif event.char == 's': # Moving backward
        display.move()
        t.setServo(0, 6000 + (SPEED * ROTATION * 4))
        time.sleep(0.8)
        t.reset(0)
    elif(event.char == '='): # incrememnt speed
        SPEED = SPEED + 1
        if(SPEED == 4):
            SPEED = 1
    elif event.char == 'a': # Turning left
        display.drawEyes(2)
        t.setServo(1, 6000 + (SPEED * ROTATION * 6))
        time.sleep(0.6)
        t.reset(1)
    elif event.char == 'd': # Turning right
        display.drawEyes(4)
        t.setServo(1, 6000 - (SPEED * ROTATION * 6))
        time.sleep(0.6)
        t.reset(1)
    elif event.char == '-': # Changing direction
        DIRECTION *= -1

    # HEAD & WAIST
    elif event.char == 'z': # Moving waist
        if DIRECTION == 1:
            display.drawEyes(2)
        else:
            display.drawEyes(4)
        t.moveServo(2, ROTATION * DIRECTION * 2)
    elif event.char == ',': # Turning head
        if DIRECTION == 1:
            display.drawEyes(2)
        else:
            display.drawEyes(4)
        t.moveServo(3, ROTATION * DIRECTION)
    elif event.char == '.': # Tilting head
        if DIRECTION == 1:
            display.drawEyes(1)
        else:
            display.drawEyes(3)
        t.moveServo(4, ROTATION * DIRECTION)

    # RIGHT ARM
    elif event.char == 't': # right shoulder
        display.drawEyes(5)
        t.moveServo(5, ROTATION * DIRECTION)
    elif event.char == 'y': # right bicep
        display.drawEyes(5)
        t.moveServo(6, ROTATION * DIRECTION)
    elif event.char == 'u': # right elbow
        display.drawEyes(5)
        t.moveServo(7, ROTATION * DIRECTION)
    elif event.char == 'i': #right forearm
        display.drawEyes(5)
        t.moveServo(8, ROTATION * DIRECTION)
    elif event.char == 'o': # right wrist
        display.drawEyes(5)
        t.moveServo(9, ROTATION * DIRECTION)
    elif event.char == 'p': # right gripper
        display.drawEyes(5)
        t.moveServo(10, ROTATION * DIRECTION)

    # LEFT ARM
    elif event.char == 'f': # left shoulder
        display.drawEyes(5)
        t.moveServo(11, ROTATION * DIRECTION)
    elif event.char == 'g': # left bicep
        display.drawEyes(5)
        t.moveServo(12, ROTATION * DIRECTION)
    elif event.char == 'h': # left elbow
        display.drawEyes(5)
        t.moveServo(13, ROTATION * DIRECTION)
    elif event.char == 'j': # left forearm
        display.drawEyes(5)
        t.moveServo(14, ROTATION * DIRECTION)
    elif event.char == 'k': # left wrist
        display.drawEyes(5)
        t.moveServo(15, ROTATION * DIRECTION)
    elif event.char == 'l': # left gripper
        display.drawEyes(5)
        t.moveServo(16, ROTATION * DIRECTION)

    # DISPLAY WORDS
    elif event.char == '1':
        gesture.start()
        display.drawEyes(5)
    elif event.char == '2':
        display.printText(text, 20)
        Thread(target=speechBot.speak, args=(text,)).start()
    elif event.char == '3':
        display.printWordSpiral(word, 150)
        Thread(target=speechBot.speak, args=(word,)).start()
    elif event.char == '4':
        display.printText(speech, 12)
        root.update_idletasks() 
        
        t1 = Thread(target=speechBot.speak, args=(speech,))
        t1.start()
        while t1.is_alive():
            gesture.randomGesture()
            time.sleep(0.8)

        gesture.stopLoop()
        display.drawEyes(5)
        gesture.start()
    elif event.char == '5':
        display.printText(speech, 12)
    
def run(root):
    global DIRECTION
    DIRECTION = 1

    tango = Tango()
    display = Screen(root)
    speech = TTS()
    gesture = Gesture(tango)
    gesture.start()

    root.bind("<Key>", lambda event: key_pressed(event, tango, display, gesture, speech))

if __name__ == "__main__":
    root=tk.Tk()
    run(root)
    root.mainloop()