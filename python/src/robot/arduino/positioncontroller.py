import time
from python.src.robot.arduino.arduinointerface import ArduinoInterface
from python.src.robot.logger import Logger

class PositionController:
    def __init__(self):
        self.arduinoInterface = ArduinoInterface.getInstance()

    def advance(self, distanceInCentimeters):
        ser = self.arduinoInterface.connect()

        distanceInMillimeters = int(round(distanceInCentimeters * 10, 0))

        Logger.logEverywhere("ROBOT: advancing of " + str(distanceInMillimeters) + " mm")

        self.arduinoInterface.write(ser, 'D' + str(distanceInMillimeters) + '.')
        self.arduinoInterface.write(ser, 'A0.')
        self.arduinoInterface.write(ser, 'V150.')
        self.arduinoInterface.write(ser, 'M.')

        self.arduinoInterface.checkIfOperationIsOver(ser)

    def rotate(self, angleInDegrees):
        ser = self.arduinoInterface.connect()

        angleInDegrees = int(round(angleInDegrees, 0))

        Logger.logEverywhere("ROBOT: rotating of " + str(angleInDegrees) + " degrees")

        self.arduinoInterface.write(ser, 'R' + str(angleInDegrees) + '.')

        self.arduinoInterface.checkIfOperationIsOver(ser)

    def shuffle(self, distanceInCentimeters, relativeAngleInDegrees):
        ser = self.arduinoInterface.connect()

        distanceInMillimeters = int(round(distanceInCentimeters * 10, 0))
        relativeAngleInDegrees = int(round(relativeAngleInDegrees, 0))

        Logger.logEverywhere("ROBOT: shuffling of " + str(distanceInMillimeters) + " mm at angle " + str(
            relativeAngleInDegrees) + " degrees")

        self.arduinoInterface.write(ser, 'D' + str(distanceInMillimeters) + '.')
        self.arduinoInterface.write(ser, 'A' + str(relativeAngleInDegrees) + '.')
        self.arduinoInterface.write(ser, 'V50.')
        self.arduinoInterface.write(ser, 'M.')

        self.arduinoInterface.checkIfOperationIsOver(ser)
