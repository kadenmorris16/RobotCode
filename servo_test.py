from maestro import Controller

HEADTURN = 4

class Tango:
    def __init__(self):
        self.tango = Controller()
        self.turn = 4500
        self.tango.setTarget(HEADTURN, self.turn)


t = Tango()