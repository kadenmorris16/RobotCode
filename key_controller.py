from tkinter import Tk, Label
#from maestro import Controller

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

root=Tk()

class Tango:
    def __init__(self):
        self.tango = Controller()
        self.turn = 4500
        self.tango.setTarget(HEADTURN, self.turn)
    
    def moveServo(self, port, val):
        self.tango.setTarget(port, val)


#t = Tango()

def key_pressed(event):
    pressed = event.char
    if(pressed == 'w'):
        w=Label(root,text="Moving forward")
        #t.moveServo(0, 4500)
    elif(pressed == 's'):
        w=Label(root,text="Moving backwards")
        #t.moveServo(0, 7500)
    elif(pressed == 'a'):
        w=Label(root,text="Turning left")
    elif(pressed == 'd'):
        w=Label(root,text="Turning right")
    else:
        w=Label(root,text="Key Pressed: "+ pressed)

    w.place(x=70,y=90)

root.bind("<Key>",key_pressed)

root.mainloop()