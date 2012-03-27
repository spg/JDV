import time
from python.src.robot.arduino.prehensorcontroller import PrehensorController

prehensorController = PrehensorController()
prehensorController.dropPrehensor()
time.sleep(5)
prehensorController.raisePrehensor()