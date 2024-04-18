from tango import Tango
from threading import Thread
import time

class Gesture:
    def __init__(self, tango):
        self.t = tango

    def reset(self): # left arm does not reset right
        for i in range(14):
            self.t.reset(i+2)

    def start(self):
        self.t.setServo(2, 1500 * 4) # waist (+ = left)
        self.t.setServo(3, 1500 * 4) # turn head (+ = left)
        self.t.setServo(4, 1500 * 4) # tilt head (+ = up)
        self.t.setServo(5, 1190 * 4) # r shoulder (+ = up)
        self.t.setServo(6, 1650 * 4) # r bicep (+ = out)
        self.t.setServo(7, 1500 * 4) # r elbow (+ = up)
        self.t.setServo(8, 1690 * 4) # r forearm (+ = up)
        self.t.setServo(9, 1400 * 4) # r wrist (+ = rotate left)
        self.t.setServo(10, 1000 * 4) # r gripper (+ = close)
        self.t.setServo(11, 1650 * 4) # l shoulder (+ = down)
        self.t.setServo(12, 1150 * 4) # l bicep (+ = in)
        self.t.setServo(13, 1150 * 4) # l elbow (+ = up)
        self.t.setServo(14, 1750 * 4) # l forearm (+ = up)
        self.t.setServo(15, 1550 * 4) # l wrist (+ = rotate left)
        self.t.setServo(16, 1500 * 4) # l gripper (+ = close)

    def armsUp(self):
        Thread(target=self.smoothMove, args=(2, 1500 * 4,)).start() # waist (+ = left)
        Thread(target=self.smoothMove, args=(3, 1500 * 4,)).start() # turn head (+ = left)
        Thread(target=self.smoothMove, args=(4, 1500 * 4,)).start() # tilt head (+ = up)
        Thread(target=self.smoothMove, args=(5, 2000 * 4,)).start() # r shoulder (+ = up)
        Thread(target=self.smoothMove, args=(6, 1650 * 4,)).start() # r bicep (+ = out)
        Thread(target=self.smoothMove, args=(7, 1500 * 4,)).start() # r elbow (+ = up)
        Thread(target=self.smoothMove, args=(8, 1690 * 4,)).start() # r forearm (+ = up)
        Thread(target=self.smoothMove, args=(9, 1400 * 4,)).start() # r wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(10, 1000 * 4,)).start() # r gripper (+ = close)
        Thread(target=self.smoothMove, args=(11, 992 * 4,)).start() # l shoulder (+ = down)
        Thread(target=self.smoothMove, args=(12, 1150 * 4,)).start() # l bicep (+ = in)
        Thread(target=self.smoothMove, args=(13, 1150 * 4,)).start() # l elbow (+ = up)
        Thread(target=self.smoothMove, args=(14, 1750 * 4,)).start() # l forearm (+ = up)
        Thread(target=self.smoothMove, args=(15, 1550 * 4,)).start() # l wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(16, 1500 * 4,)).start() # l gripper (+ = close)

    def armsDown(self):
        Thread(target=self.smoothMove, args=(2, 1500 * 4,)).start() # waist (+ = left)
        Thread(target=self.smoothMove, args=(3, 1500 * 4,)).start() # turn head (+ = left)
        Thread(target=self.smoothMove, args=(4, 1500 * 4,)).start() # tilt head (+ = up)
        Thread(target=self.smoothMove, args=(5, 992 * 4,)).start() # r shoulder (+ = up)
        Thread(target=self.smoothMove, args=(6, 1650 * 4,)).start() # r bicep (+ = out)
        Thread(target=self.smoothMove, args=(7, 1500 * 4,)).start() # r elbow (+ = up)
        Thread(target=self.smoothMove, args=(8, 1690 * 4,)).start() # r forearm (+ = up)
        Thread(target=self.smoothMove, args=(9, 1400 * 4,)).start() # r wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(10, 1000 * 4,)).start() # r gripper (+ = close)
        Thread(target=self.smoothMove, args=(11, 1890 * 4,)).start() # l shoulder (+ = down)
        Thread(target=self.smoothMove, args=(12, 1150 * 4,)).start() # l bicep (+ = in)
        Thread(target=self.smoothMove, args=(13, 1150 * 4,)).start() # l elbow (+ = up)
        Thread(target=self.smoothMove, args=(14, 1750 * 4,)).start() # l forearm (+ = up)
        Thread(target=self.smoothMove, args=(15, 1550 * 4,)).start() # l wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(16, 1500 * 4,)).start() # l gripper (+ = close)

    def armsOut(self):
        pass

    def armsIn(self):
        pass

    def pointLeft(self):
        pass

    def pointRight(self):
        pass

    def reachOut(self):
        pass

    def handsOnHip(self):
        pass

    def armsCrossed(self):
        pass

    def armsPondering(self):
        pass

    def headUp(self):
        pass

    def headDown(self):
        pass

    def headLeft(self):
        pass

    def headRight(self):
        pass

    def torsoLeft(self):
        pass

    def torsoRight(self):
        pass

    def smoothMove(self, port, finalPosition):
        self.t.setSpeed(port, 1)
        self.t.setServo(port, finalPosition)
        self.t.setSpeed(port, 30)

        # movement = 100
        # position = self.t.getPosition(port)
        # print(port, "-", position, finalPosition)
        # if position > finalPosition:
        #     direction = -1
        # else:
        #     direcion = 1
        # while position != finalPosition:
        #     if direction == -1:
        #         if(position + movement < finalPosition):
        #             self.t.setServo(port, finalPosition)
        #         else:
        #             self.t.moveServo(port, movement)
        #     else:
        #         if(position + movement > finalPosition):
        #             self.t.setServo(port, finalPosition)
        #         else:
        #             self.t.moveServo(port, movement)
        #     time.sleep(0.05)

def run(tango):
    g = Gesture(tango)
    g.start()
    time.sleep(1)
    g.armsUp()
    time.sleep(1)
    g.armsDown()


if __name__ == "__main__":
    tango = Tango()
    run(tango)