from serial import Serial
import time
from python.src.robot.logger import Logger

class ArduinoInterface:
    instance = None

    def __init__(self):
        self.ser = Serial('/dev/ttyACM0', 115200)
        time.sleep(2)

        time.sleep(1)
        self.ser.setDTR(level=0)
        time.sleep(1)

    @staticmethod
    def getInstance():
        if ArduinoInterface.instance is None:
            ArduinoInterface.instance = ArduinoInterface()
        return ArduinoInterface.instance

    def connect(self):
        ser = self.ser

        return ser

    def checkIfOperationIsOver(self, ser):

        operationOver = False

        while not operationOver:
            time.sleep(0.1)
            line = ser.readline()
            print "arduino: " + str(line)
            if line.find("over") != -1:
                logger = Logger.logToFileAndScreen("operation over")
                operationOver = True

    def readLine(self, ser):
        return ser.readline()
