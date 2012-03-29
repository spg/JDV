import time
from python.src.robot.arduino.arduinointerface import ArduinoInterface
from python.src.robot.logger import Logger

class PositionController:
    def __init__(self):
        self.arduinoInterface = ArduinoInterface.getInstance()

    def advance(self, distanceInCentimeters):
        ser = self.arduinoInterface.connect()

        Logger.logEverywhere("ROBOT: advancing of " + str(distanceInCentimeters) + " cm")

        time.sleep(0.1)
        ser.write('D' + str(distanceInCentimeters) + '.')
        time.sleep(0.1)
        ser.write('A0.')
        time.sleep(0.1)
        ser.write('V40.')
        time.sleep(0.1)
        ser.write('M.')

        self.arduinoInterface.checkIfOperationIsOver(ser)

    def rotate(self, angleInDegrees):
        ser = self.arduinoInterface.connect()

        Logger.logEverywhere("ROBOT: rotating of " + str(angleInDegrees) + " degrees")

        ser.write('R' + str(angleInDegrees) + '.')

        self.arduinoInterface.checkIfOperationIsOver(ser)

    def shuffle(self, distanceInCentimeters, relativeAngleInDegrees):
        ser = self.arduinoInterface.connect()

        Logger.logEverywhere("ROBOT: shuffling of " + str(distanceInCentimeters) + " cm at angle " + str(
            relativeAngleInDegrees) + " degrees")

        ser.write('D' + str(distanceInCentimeters) + '.')
        ser.write('A' + str(relativeAngleInDegrees) + '.')
        ser.write('V5.')
        ser.write('M.')

        self.arduinoInterface.checkIfOperationIsOver(ser)