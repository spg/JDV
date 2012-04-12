from serial import Serial
import time
from serial.serialutil import SerialException
from python.src.robot.logger import Logger

class ArduinoInterface:
    instance = None

    def __init__(self):
        self.ser = Serial()
        self.ser.baudrate = 115200

        for portId in range(0, 5):
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
        print "checking if operation is over..."
        operationOver = False

        while not operationOver:
            print "entered while in checkIfOperationIsOver"
            time.sleep(0.1)
            print "reading line in checkIfOperationIsOver"
            line = self.ser.readline()
            print "arduino: " + str(line)
            if line.find("over") != -1:
                Logger.logToFileAndScreen("operation over")
                operationOver = True

        print "returning out of checkIfOperationIsOver"

    def write(self, message):
        print "message to write: " + str(message)
        operationBegun = False

        while not operationBegun:
            print "before writing message in write method..."
            self.ser.flushInput()
            self.ser.write(message)
            print "after writing message in write method..."
            time.sleep(0.5)
            print "after sleeping"
            operationBegun = self.checkIfOperationHasBegun()

        print "returning out of write(self, message)"

    def checkIfOperationHasBegun(self):
        return True
        print "before reading ling in checkIfOperationHasBegun"
        line = self.ser.readline()
        print "in checkIfOperationHasBegun - ARDUINO: " + str(line)
        if line.find("okay") != -1:
            return True
        return False

    def readLine(self):
        line = self.ser.readline()
        return line
