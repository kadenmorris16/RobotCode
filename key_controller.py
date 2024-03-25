from tkinter import Tk, Label
from tango import Tango
from proj3_threads import Screen
import time

def key_pressed(event, t, display):
    pressed = event.char

    # Movement variables
    ROTATION = 200
    DIRECTION = 1
    SPEED = 1   

    # WHEELS
    if(pressed == 'w'):
        display.move()
        #w=Label(root,text="Moving forward")
        t.setServo(0, 6000 - (SPEED * ROTATION * 4))
        time.sleep(1)
        t.reset(0)
    elif(pressed == 's'):
        display.move()
        #w=Label(root,text="Moving backwards")
        t.setServo(0, 6000 + (SPEED * ROTATION * 4))
        time.sleep(1)
        t.reset(0)
    elif(pressed == '='):
        #w=Label(root,text="Incrementing speed")
        SPEED = SPEED + 1
        if(SPEED == 4):
            SPEED = 1
    elif(pressed == 'a'):
        display.move()
        #w=Label(root,text="Turning left")
        t.setServo(1, 6000 + (SPEED * ROTATION * 4))
        time.sleep(1)
        t.reset(1)
    elif(pressed == 'd'):
        display.move()
        #w=Label(root,text="Turning right")
        t.setServo(1, 6000 - (SPEED * ROTATION * 4))
        time.sleep(1)
        t.reset(1)
    elif(pressed == '-'):
        #w=Label(root,text="Changing direction")
        DIRECTION *= -1

    # HEAD & WAIST
    elif(pressed == 'z'):
        display.drawEyes(0)
        #w=Label(root,text="Moving waist")
        t.moveServo(2, ROTATION * DIRECTION)
    elif(pressed == ','):
        display.drawEyes(0)
        #w=Label(root,text="Turning head")
        t.moveServo(3, ROTATION * DIRECTION)
    elif(pressed == '.'):
        display.drawEyes(0)
        #w=Label(root,text="Tilting head")
        t.moveServo(4, ROTATION * DIRECTION)

    # RIGHT ARM
    elif(pressed == 't'):
        display.drawEyes(0)
        #w=Label(root,text="Moving right shoulder")
        t.moveServo(5, ROTATION * DIRECTION)
    elif(pressed == 'y'):
        display.drawEyes(0)
        #w=Label(root,text="Moving right bicep")
        t.moveServo(6, ROTATION * DIRECTION)
    elif(pressed == 'u'):
        display.drawEyes(0)
        #w=Label(root,text="Moving right elbow")
        t.moveServo(7, ROTATION * DIRECTION)
    elif(pressed == 'i'):
        display.drawEyes(0)
        #w=Label(root,text="Moving right forearm")
        t.moveServo(8, ROTATION * DIRECTION)
    elif(pressed == 'o'):
        display.drawEyes(0)
        #w=Label(root,text="Moving right wrist")
        t.moveServo(9, ROTATION * DIRECTION)
    elif(pressed == 'p'):
        display.drawEyes(0)
        #w=Label(root,text="Moving right gripper")
        t.moveServo(10, ROTATION * DIRECTION)

    # LEFT ARM
    elif(pressed == 'f'):
        display.drawEyes(0)
        #w=Label(root,text="Moving left shoulder")
        t.moveServo(11, ROTATION * DIRECTION)
    elif(pressed == 'g'):
        display.drawEyes(0)
        #w=Label(root,text="Moving left bicep")
        t.moveServo(12, ROTATION * DIRECTION)
    elif(pressed == 'h'):
        display.drawEyes(0)
        #w=Label(root,text="Moving left elbow")
        t.moveServo(13, ROTATION * DIRECTION)
    elif(pressed == 'j'):
        display.drawEyes(0)
        #w=Label(root,text="Moving left forearm")
        t.moveServo(14, ROTATION * DIRECTION)
    elif(pressed == 'k'):
        display.drawEyes(0)
        #w=Label(root,text="Moving left wrist")
        t.moveServo(15, ROTATION * DIRECTION)
    elif(pressed == 'l'):
        display.drawEyes(0)
        #w=Label(root,text="Moving left gripper")
        t.moveServo(16, ROTATION * DIRECTION)
    else:
        display.drawEyes(0)
        #w=Label(root,text="Key Pressed: "+ pressed)

    #w.place(x=70,y=90)
        
def run():
    root=Tk()
    root.withdraw()
    tango = Tango()
    display = Screen()
    root.bind("<Key>", lambda event: key_pressed(event, tango, display))
    root.mainloop()

if __name__ == "__main__":
    run()