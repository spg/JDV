from serial import Serial
import time
from serial.serialutil import SerialException
from python.src.robot.logger import Logger

class ArduinoInterface:
    instance = None

    def __init__(self):
        self.ser = Serial()
        self.ser.baudrate = 115200

        for portId in range(0, 4):
            portName = '/dev/ttyACM' + str(portId)
            self.ser.port = portName
            try:
                print "trying to open USB port " + str(portName)
                self.ser.open()
                break
            except SerialException :
                print "could not open USB port " + str(portName)
                pass


        time.sleep(2)

        time.sleep(1)
        self.ser.setDTR(level=0)
        time.sleep(1)

    @staticmethod
    def getInstance():
        if ArduinoInterface.instance is None:
            ArduinoInterface.instance = ArduinoInterface()
        return ArduinoInterface.instance

    def checkIfOperationIsOver(self):
        operationOver = False

        while not operationOver:
            time.sleep(0.1)
            line = self.ser.readline()
            print "arduino: " + str(line)
            if line.find("over") != -1:
                Logger.logToFileAndScreen("operation over")
                operationOver = True

    def write(self, message):
        operationBegun = False

        while not operationBegun:
            self.ser.write(message)
            time.sleep(0.5)
            operationBegun = self.checkIfOperationHasBegun()

    def checkIfOperationHasBegun(self):
        line = self.ser.readline()
        print "in checkIfOperationHasBegun - ARDUINO: " + str(line)
        if line.find("okay") != -1:
            return True
        return False

    def readLine(self):
        return self.ser.readline()
