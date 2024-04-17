from tango import Tango

class Gesture:
    def __init__(self, tango):
        self.t = tango

    def reset(self):
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



def run(tango):
    g = Gesture(tango)
    g.start()


if __name__ == "__main__":
    tango = Tango()
    run(tango)