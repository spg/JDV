from serial import Serial
import time
from python.src.robot.logger import Logger

class ArduinoInterface:
    def connect(self):
        ser = Serial('/dev/ttyACM0', 115200)

        time.sleep(1)
        ser.setDTR(level=0)
        time.sleep(1)

        return ser

    def checkIfOperationIsOver(self, ser):

        operationOver = False

        while not operationOver:
            time.sleep(0.1)
            line = ser.readline()
            if line.find("over") != -1:
                logger = Logger.logToFileAndScreen("operation over")
                operationOver = True
