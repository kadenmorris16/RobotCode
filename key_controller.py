from tkinter import Tk, Label
from maestro import Controller

# Port Declarations
FORWARD_REVERSE = 0
LEFT_RIGHT = 1
WAIST = 2
HEADTILT = 3
HEADTURN = 4
R_SHOULDER = 5
R_BICEP = 6
R_ELBOW = 7
R_FOREARM = 8
R_WRIST = 9
R_GRIPPER = 10
L_SHOULDER = 11
L_BICEP = 12
L_ELBOW = 13
L_FOREARM = 14
L_WRIST = 15
L_GRIPPER = 16

# Movement variables
ROTATION = 200
direction = 1
SPEED = 1

root=Tk()

class Tango:
    def __init__(self):
        self.tango = Controller()
        self.turn = 4500
        self.tango.setTarget(HEADTURN, self.turn)
    
    def moveServo(self, port, val):
        self.tango.setTarget(port, self.tango.getPosition(port) + val)


t = Tango()

def key_pressed(event):
    pressed = event.char
    global direction
    # WHEELS
    if(pressed == 'w'):
        w=Label(root,text="Moving forward")
        t.moveServo(0, ROTATION * SPEED)
    elif(pressed == 's'):
        w=Label(root,text="Moving backwards")
        t.moveServo(0, -1 * ROTATION * SPEED)
    elif(pressed == 'a'):
        w=Label(root,text="Turning left")
        t.moveServo(1, -1 * ROTATION)
    elif(pressed == 'd'):
        w=Label(root,text="Turning right")
        t.moveServo(1, ROTATION)
    elif(pressed == '-'):
        w=Label(root,text="Changing direction")
        direction *= -1

    # HEAD & WAIST
    elif(pressed == 'z'):
        w=Label(root,text="Moving waist")
        t.moveServo(2, ROTATION * direction)
    elif(pressed == ','):
        w=Label(root,text="Turning head")
        t.moveServo(3, ROTATION * direction)
    elif(pressed == '.'):
        w=Label(root,text="Tilting head")
        t.moveServo(4, ROTATION * direction)

    # RIGHT ARM
    elif(pressed == 't'):
        w=Label(root,text="Moving right shoulder")
        t.moveServo(5, ROTATION * direction)
    elif(pressed == 'y'):
        w=Label(root,text="Moving right bicep")
        t.moveServo(6, ROTATION * direction)
    elif(pressed == 'u'):
        w=Label(root,text="Moving right elbow")
        t.moveServo(7, ROTATION * direction)
    elif(pressed == 'i'):
        w=Label(root,text="Moving right forearm")
        t.moveServo(8, ROTATION * direction)
    elif(pressed == 'o'):
        w=Label(root,text="Moving right wrist")
        t.moveServo(9, ROTATION * direction)
    elif(pressed == 'p'):
        w=Label(root,text="Moving right gripper")
        t.moveServo(10, ROTATION * direction)

    # LEFT ARM
    elif(pressed == 'f'):
        w=Label(root,text="Moving left shoulder")
        t.moveServo(11, ROTATION * direction)
    elif(pressed == 'g'):
        w=Label(root,text="Moving left bicep")
        t.moveServo(12, ROTATION * direction)
    elif(pressed == 'h'):
        w=Label(root,text="Moving left elbow")
        t.moveServo(13, ROTATION * direction)
    elif(pressed == 'j'):
        w=Label(root,text="Moving left forearm")
        t.moveServo(14, ROTATION * direction)
    elif(pressed == 'k'):
        w=Label(root,text="Moving left wrist")
        t.moveServo(15, ROTATION * direction)
    elif(pressed == 'l'):
        w=Label(root,text="Moving left gripper")
        t.moveServo(16, ROTATION * direction)
    else:
        w=Label(root,text="Key Pressed: "+ pressed)

    w.place(x=70,y=90)

root.bind("<Key>",key_pressed)

root.mainloop()