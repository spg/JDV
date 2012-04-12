import time
from python.src.robot.arduino.ledcontroller import LedController

ledController = LedController()

while True:

    ledController.turnLedOn()
    time.sleep(0.2)
    ledController.turnLedOff()