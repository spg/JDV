import time
from python.src.robot.arduino.ledcontroller import LedController

ledController = LedController()

ledController.turnLedOn()
time.sleep(1)
ledController.turnLedOff()
time.sleep(1)
ledController.turnLedOn()