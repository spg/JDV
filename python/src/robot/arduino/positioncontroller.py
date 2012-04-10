from python.src.robot.arduino.arduinointerface import ArduinoInterface
from python.src.robot.logger import Logger

class PositionController:
    def __init__(self):
        self.arduinoInterface = ArduinoInterface.getInstance()

    def advance(self, distanceInCentimeters):
        distanceInMillimeters = int(round(distanceInCentimeters * 10, 0))

        Logger.logEverywhere("ROBOT: advancing of " + str(distanceInMillimeters) + " mm")

        self.arduinoInterface.write('D' + str(distanceInMillimeters) + '.')
        self.arduinoInterface.write('A0.')
        self.arduinoInterface.write('V150.')
        self.arduinoInterface.write('M.')

        self.arduinoInterface.checkIfOperationIsOver()

    def rotate(self, angleInDegrees):
        angleInDegrees = int(round(angleInDegrees, 0))

        Logger.logEverywhere("ROBOT: rotating of " + str(angleInDegrees) + " degrees")

        self.arduinoInterface.write('R' + str(angleInDegrees) + '.')

        self.arduinoInterface.checkIfOperationIsOver()

    def shuffle(self, distanceInCentimeters, relativeAngleInDegrees):
        distanceInMillimeters = int(round(distanceInCentimeters * 10, 0))
        relativeAngleInDegrees = int(round(relativeAngleInDegrees, 0))

        Logger.logEverywhere("ROBOT: shuffling of " + str(distanceInMillimeters) + " mm at angle " + str(
            relativeAngleInDegrees) + " degrees")

        self.arduinoInterface.write('D' + str(distanceInMillimeters) + '.')
        self.arduinoInterface.write('A' + str(relativeAngleInDegrees) + '.')
        self.arduinoInterface.write('V50.')
        self.arduinoInterface.write('M.')

        self.arduinoInterface.checkIfOperationIsOver()
