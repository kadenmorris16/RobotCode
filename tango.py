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

class Tango:
    def __init__(self):
        self.tango = Controller()
        self.turn = 4500
        self.tango.setTarget(HEADTURN, self.turn)
        self.tango.setTarget(FORWARD_REVERSE, 6000)
        self.tango.setTarget(LEFT_RIGHT, 6000)
    
    def moveServo(self, port, val):
        self.tango.setTarget(port, self.tango.getPosition(port) + val)
        return
    
    def setServo(self, port, val):
        self.tango.setTarget(port, val)
        return
    
    def reset(self, port):
        self.tango.setTarget(port, 6000)
        return
    
    def getPosition(self, port):
        return self.tango.getPosition(port)
    
    def setSpeed(self, port, speed):
        self.tango.setSpeed(port, speed)
        return