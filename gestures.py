from tango import Tango
from threading import Thread
import time
import random

class Gesture:
    def __init__(self, tango):
        self.t = tango
        self.stopFlag = False

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
        Thread(target=self.smoothMove, args=(5, 1900 * 4,)).start() # r shoulder (+ = up)
        Thread(target=self.smoothMove, args=(6, 1700 * 4,)).start() # r bicep (+ = out)
        Thread(target=self.smoothMove, args=(7, 1990 * 4,)).start() # r elbow (+ = up)
        Thread(target=self.smoothMove, args=(8, 1575 * 4,)).start() # r forearm (+ = up)
        Thread(target=self.smoothMove, args=(9, 1400 * 4,)).start() # r wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(10, 1000 * 4,)).start() # r gripper (+ = close)
        Thread(target=self.smoothMove, args=(11, 992 * 4,)).start() # l shoulder (+ = down)
        Thread(target=self.smoothMove, args=(12, 1150 * 4,)).start() # l bicep (+ = in)
        Thread(target=self.smoothMove, args=(13, 1670 * 4,)).start() # l elbow (+ = up)
        Thread(target=self.smoothMove, args=(14, 1700 * 4,)).start() # l forearm (+ = up)
        Thread(target=self.smoothMove, args=(15, 1490 * 4,)).start() # l wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(16, 1500 * 4,)).start() # l gripper (+ = close)

    def armsDown(self):
        Thread(target=self.smoothMove, args=(5, 1400 * 4,)).start() # r shoulder (+ = up)
        Thread(target=self.smoothMove, args=(6, 1500 * 4,)).start() # r bicep (+ = out)
        Thread(target=self.smoothMove, args=(7, 1350 * 4,)).start() # r elbow (+ = up)
        Thread(target=self.smoothMove, args=(8, 1425 * 4,)).start() # r forearm (+ = up)
        Thread(target=self.smoothMove, args=(9, 1500 * 4,)).start() # r wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(10, 1000 * 4,)).start() # r gripper (+ = close)
        Thread(target=self.smoothMove, args=(11, 1500 * 4,)).start() # l shoulder (+ = down)
        Thread(target=self.smoothMove, args=(12, 1250 * 4,)).start() # l bicep (+ = in)
        Thread(target=self.smoothMove, args=(13, 992 * 4,)).start() # l elbow (+ = up)
        Thread(target=self.smoothMove, args=(14, 1550 * 4,)).start() # l forearm (+ = up)
        Thread(target=self.smoothMove, args=(15, 1390 * 4,)).start() # l wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(16, 1480 * 4,)).start() # l gripper (+ = close)

    def armsOut(self):
        Thread(target=self.smoothMove, args=(5, 1775 * 4,)).start() # r shoulder (+ = up)
        Thread(target=self.smoothMove, args=(6, 1300 * 4,)).start() # r bicep (+ = out)
        Thread(target=self.smoothMove, args=(7, 1320 * 4,)).start() # r elbow (+ = up)
        Thread(target=self.smoothMove, args=(8, 1540 * 4,)).start() # r forearm (+ = up)
        Thread(target=self.smoothMove, args=(9, 1600 * 4,)).start() # r wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(10, 1000 * 4,)).start() # r gripper (+ = close)
        Thread(target=self.smoothMove, args=(11, 1060 * 4,)).start() # l shoulder (+ = down)
        Thread(target=self.smoothMove, args=(12, 1475 * 4,)).start() # l bicep (+ = in)
        Thread(target=self.smoothMove, args=(13, 992 * 4,)).start() # l elbow (+ = up)
        Thread(target=self.smoothMove, args=(14, 1530 * 4,)).start() # l forearm (+ = up)
        Thread(target=self.smoothMove, args=(15, 1410 * 4,)).start() # l wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(16, 1500 * 4,)).start() # l gripper (+ = close)

    def armsIn(self):
        Thread(target=self.smoothMove, args=(5, 1820 * 4,)).start() # r shoulder (+ = up)
        Thread(target=self.smoothMove, args=(6, 1460 * 4,)).start() # r bicep (+ = out)
        Thread(target=self.smoothMove, args=(7, 1865 * 4,)).start() # r elbow (+ = up)
        Thread(target=self.smoothMove, args=(8, 1890 * 4,)).start() # r forearm (+ = up)
        Thread(target=self.smoothMove, args=(9, 1600 * 4,)).start() # r wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(10, 1000 * 4,)).start() # r gripper (+ = close)
        Thread(target=self.smoothMove, args=(11, 1060 * 4,)).start() # l shoulder (+ = down)
        Thread(target=self.smoothMove, args=(12, 1315 * 4,)).start() # l bicep (+ = in)
        Thread(target=self.smoothMove, args=(13, 1650 * 4,)).start() # l elbow (+ = up)
        Thread(target=self.smoothMove, args=(14, 1820 * 4,)).start() # l forearm (+ = up)
        Thread(target=self.smoothMove, args=(15, 1430 * 4,)).start() # l wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(16, 1500 * 4,)).start() # l gripper (+ = close)

    def pointLeftDouble(self):
        Thread(target=self.smoothMove, args=(5, 1950 * 4,)).start() # r shoulder (+ = up)
        Thread(target=self.smoothMove, args=(6, 992 * 4,)).start() # r bicep (+ = out)
        Thread(target=self.smoothMove, args=(7, 1180 * 4,)).start() # r elbow (+ = up)
        Thread(target=self.smoothMove, args=(8, 1400 * 4,)).start() # r forearm (+ = up)
        Thread(target=self.smoothMove, args=(9, 2000 * 4,)).start() # r wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(10, 2000 * 4,)).start() # r gripper (+ = close)
        Thread(target=self.smoothMove, args=(11, 992 * 4,)).start() # l shoulder (+ = down)
        Thread(target=self.smoothMove, args=(12, 992 * 4,)).start() # l bicep (+ = in)
        Thread(target=self.smoothMove, args=(13, 992 * 4,)).start() # l elbow (+ = up)
        Thread(target=self.smoothMove, args=(14, 1560 * 4,)).start() # l forearm (+ = up)
        Thread(target=self.smoothMove, args=(15, 1930 * 4,)).start() # l wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(16, 2000 * 4,)).start() # l gripper (+ = close)

    def pointRightDouble(self):
        Thread(target=self.smoothMove, args=(5, 1950 * 4,)).start() # r shoulder (+ = up)
        Thread(target=self.smoothMove, args=(6, 2000 * 4,)).start() # r bicep (+ = out)
        Thread(target=self.smoothMove, args=(7, 1260 * 4,)).start() # r elbow (+ = up)
        Thread(target=self.smoothMove, args=(8, 1415 * 4,)).start() # r forearm (+ = up)
        Thread(target=self.smoothMove, args=(9, 992 * 4,)).start() # r wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(10, 2000 * 4,)).start() # r gripper (+ = close)
        Thread(target=self.smoothMove, args=(11, 992 * 4,)).start() # l shoulder (+ = down)
        Thread(target=self.smoothMove, args=(12, 2000 * 4,)).start() # l bicep (+ = in)
        Thread(target=self.smoothMove, args=(13, 992 * 4,)).start() # l elbow (+ = up)
        Thread(target=self.smoothMove, args=(14, 1430 * 4,)).start() # l forearm (+ = up)
        Thread(target=self.smoothMove, args=(15, 1360 * 4,)).start() # l wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(16, 2000 * 4,)).start() # l gripper (+ = close)

    def pointLeftSingle(self):
        Thread(target=self.smoothMove, args=(5, 1400 * 4,)).start() # r shoulder (+ = up)
        Thread(target=self.smoothMove, args=(6, 1710 * 4,)).start() # r bicep (+ = out)
        Thread(target=self.smoothMove, args=(7, 1960 * 4,)).start() # r elbow (+ = up)
        Thread(target=self.smoothMove, args=(8, 1565 * 4,)).start() # r forearm (+ = up)
        Thread(target=self.smoothMove, args=(9, 1420 * 4,)).start() # r wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(10, 1220 * 4,)).start() # r gripper (+ = close)
        Thread(target=self.smoothMove, args=(11, 992 * 4,)).start() # l shoulder (+ = down)
        Thread(target=self.smoothMove, args=(12, 992 * 4,)).start() # l bicep (+ = in)
        Thread(target=self.smoothMove, args=(13, 992 * 4,)).start() # l elbow (+ = up)
        Thread(target=self.smoothMove, args=(14, 1560 * 4,)).start() # l forearm (+ = up)
        Thread(target=self.smoothMove, args=(15, 1930 * 4,)).start() # l wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(16, 2000 * 4,)).start() # l gripper (+ = close)

    def pointRightSingle(self):
        Thread(target=self.smoothMove, args=(5, 1950 * 4,)).start() # r shoulder (+ = up)
        Thread(target=self.smoothMove, args=(6, 2000 * 4,)).start() # r bicep (+ = out)
        Thread(target=self.smoothMove, args=(7, 1260 * 4,)).start() # r elbow (+ = up)
        Thread(target=self.smoothMove, args=(8, 1415 * 4,)).start() # r forearm (+ = up)
        Thread(target=self.smoothMove, args=(9, 992 * 4,)).start() # r wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(10, 2000 * 4,)).start() # r gripper (+ = close)
        Thread(target=self.smoothMove, args=(11, 1500 * 4,)).start() # l shoulder (+ = down)
        Thread(target=self.smoothMove, args=(12, 1080 * 4,)).start() # l bicep (+ = in)
        Thread(target=self.smoothMove, args=(13, 1500 * 4,)).start() # l elbow (+ = up)
        Thread(target=self.smoothMove, args=(14, 1890 * 4,)).start() # l forearm (+ = up)
        Thread(target=self.smoothMove, args=(15, 1480 * 4,)).start() # l wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(16, 1630 * 4,)).start() # l gripper (+ = close)

    def armsCrossed(self):
        Thread(target=self.smoothMove, args=(5, 1770 * 4,)).start() # r shoulder (+ = up)
        Thread(target=self.smoothMove, args=(6, 992 * 4,)).start() # r bicep (+ = out)
        Thread(target=self.smoothMove, args=(7, 1220 * 4,)).start() # r elbow (+ = up)
        Thread(target=self.smoothMove, args=(8, 1425 * 4,)).start() # r forearm (+ = up)
        Thread(target=self.smoothMove, args=(9, 1215 * 4,)).start() # r wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(10, 1170 * 4,)).start() # r gripper (+ = close)
        Thread(target=self.smoothMove, args=(11, 992 * 4,)).start() # l shoulder (+ = down)
        Thread(target=self.smoothMove, args=(12, 2000 * 4,)).start() # l bicep (+ = in)
        Thread(target=self.smoothMove, args=(13, 992 * 4,)).start() # l elbow (+ = up)
        Thread(target=self.smoothMove, args=(14, 1460 * 4,)).start() # l forearm (+ = up)
        Thread(target=self.smoothMove, args=(15, 1600 * 4,)).start() # l wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(16, 1665 * 4,)).start() # l gripper (+ = close)

    def armsPondering(self):
        Thread(target=self.smoothMove, args=(4, 1400 * 4,)).start() # tilt head (+ = up)
        Thread(target=self.smoothMove, args=(5, 2000 * 4,)).start() # r shoulder (+ = up)
        Thread(target=self.smoothMove, args=(6, 992 * 4,)).start() # r bicep (+ = out)
        Thread(target=self.smoothMove, args=(7, 1970 * 4,)).start() # r elbow (+ = up)
        Thread(target=self.smoothMove, args=(8, 1290 * 4,)).start() # r forearm (+ = up)
        Thread(target=self.smoothMove, args=(9, 1580 * 4,)).start() # r wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(10, 1520 * 4,)).start() # r gripper (+ = close)
        Thread(target=self.smoothMove, args=(11, 1500 * 4,)).start() # l shoulder (+ = down)
        Thread(target=self.smoothMove, args=(12, 1080 * 4,)).start() # l bicep (+ = in)
        Thread(target=self.smoothMove, args=(13, 1500 * 4,)).start() # l elbow (+ = up)
        Thread(target=self.smoothMove, args=(14, 1890 * 4,)).start() # l forearm (+ = up)
        Thread(target=self.smoothMove, args=(15, 1480 * 4,)).start() # l wrist (+ = rotate left)
        Thread(target=self.smoothMove, args=(16, 1630 * 4,)).start() # l gripper (+ = close)

    def wave(self):
        self.start()
        for i in range(3):
            Thread(target=self.smoothMove, args=(5, 1770 * 4,)).start() # r shoulder (+ = up)
            Thread(target=self.smoothMove, args=(6, 992 * 4,)).start() # r bicep (+ = out)
            Thread(target=self.smoothMove, args=(7, 1220 * 4,)).start() # r elbow (+ = up)
            Thread(target=self.smoothMove, args=(8, 1425 * 4,)).start() # r forearm (+ = up)
            Thread(target=self.smoothMove, args=(9, 1215 * 4,)).start() # r wrist (+ = rotate left)
            Thread(target=self.smoothMove, args=(10, 1170 * 4,)).start() # r gripper (+ = close)
            time.sleep(0.3)
            Thread(target=self.smoothMove, args=(5, 1950 * 4,)).start() # r shoulder (+ = up)
            Thread(target=self.smoothMove, args=(6, 2000 * 4,)).start() # r bicep (+ = out)
            Thread(target=self.smoothMove, args=(7, 1260 * 4,)).start() # r elbow (+ = up)
            Thread(target=self.smoothMove, args=(8, 1415 * 4,)).start() # r forearm (+ = up)
            Thread(target=self.smoothMove, args=(9, 992 * 4,)).start() # r wrist (+ = rotate left)
            Thread(target=self.smoothMove, args=(10, 2000 * 4,)).start() # r gripper (+ = close)

    def headUp(self):
        self.smoothMove(4, 1750 * 4) # tilt head (+ = up)
        time.sleep(0.5)
        self.smoothMove(4, 1460 * 4) # tilt head (+ = up)

    def headDown(self):
        self.smoothMove(4, 1100 * 4) # tilt head (+ = up)
        time.sleep(0.5)
        self.smoothMove(4, 1460 * 4) # tilt head (+ = up)

    def headLeft(self):
        self.smoothMove(3, 2000 * 4) # turn head (+ = left)
        time.sleep(0.5)
        self.smoothMove(3, 1500 * 4) # turn head (+ = left)

    def headRight(self):
        self.smoothMove(3, 992 * 4) # turn head (+ = left)
        time.sleep(0.5)
        self.smoothMove(3, 1500 * 4) # turn head (+ = left)

    def torsoLeft(self):
        self.smoothMove(2, 1900 * 4) # waist (+ = left)
        time.sleep(1)
        self.smoothMove(2, 1500 * 4) # waist (+ = left)

    def torsoRight(self):
        self.smoothMove(2, 1000 * 4) # waist (+ = left)
        time.sleep(1)
        self.smoothMove(2, 1500 * 4) # waist (+ = left)

    def smoothMove(self, port, finalPosition):
        self.t.setSpeed(port, 1)
        self.t.setServo(port, finalPosition)
        self.t.setSpeed(port, 50)

    def stopLoop(self):
        self.stopFlag = True

    def randomGesture(self):
        rand = random.randint(0,15)

        if rand == 0:
            self.armsUp()
        elif rand == 1:
            self.armsDown()
        elif rand == 2:
            self.armsOut()
        elif rand == 3:
            self.armsIn()
        elif rand == 4:
            self.pointLeftDouble()
        elif rand == 5:
            self.pointRightDouble()
        elif rand == 6:
            self.pointLeftSingle()
        elif rand == 7:
            self.pointRightSingle()
        elif rand == 8:
            self.armsCrossed()
        elif rand == 9:
            self.armsPondering()
        elif rand == 10:
            self.headUp()
        elif rand == 11:
            self.headDown()
        elif rand == 12:
            self.headLeft()
        elif rand == 13:
            self.headRight()
        elif rand == 14:
            self.torsoLeft()
        elif rand == 15:
            self.torsoRight()


def run(tango):
    g = Gesture(tango)
    g.start()
    time.sleep(1)
    g.infiniteRandomGestures()


if __name__ == "__main__":
    tango = Tango()
    run(tango)