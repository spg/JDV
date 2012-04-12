import time
from python.src.robot.arduino.ledcontroller import LedController

class codeMorse:
    SHORT = "short"
    LONG = "long"
    PAUSE = "pause"

    def __init__(self):
        self.ledController = LedController()

    def doCode(self, signals):
        for code in signals:
            if code == codeMorse.SHORT:
                self.__short()
            elif code == codeMorse.LONG:
                self.__long()
            else:
                self.__pause()

    def __short(self):
        self.ledController.turnLedOn()
        self.ledController.turnLedOff()
        self.__pause()

    def __long(self):
        self.ledController.turnLedOn()
        time.sleep(1)
        self.ledController.turnLedOff()
        self.__pause()

    def __pause(self):
        time.sleep(1)

short = codeMorse.SHORT
lonng = codeMorse.LONG
pause = codeMorse.PAUSE

unicorn = [short, lonng, short, short, pause, short, short, pause, lonng, short, lonng, short, pause, lonng, lonng, lonng,
        pause, short, lonng, short, pause, lonng, short, pause, short]

lol = [short, lonng, short, short, pause, lonng, lonng, lonng, pause, short, lonng, short, short]

morseCodeer = codeMorse()
morseCodeer.doCode(lol)