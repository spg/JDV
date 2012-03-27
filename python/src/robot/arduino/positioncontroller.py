from serial import Serial
import time
from python.src.robot.logger import Logger

class PositionController:
    def advance(self, distanceInCentimeters):
        ser = Serial('/dev/ttyACM0', 115200)

        time.sleep(1)
        ser.setDTR(level=0)
        time.sleep(1)

        Logger.logEverywhere("ROBOT: advancing of " + str(distanceInCentimeters) + " cm")
        ser.write('D' + str(distanceInCentimeters) + '.')
        ser.write('A0.')
        ser.write('V5.')
        ser.write('M.')

        self.__checkIfOperationIsOver(ser)


    def rotate(self, angleInDegrees):

        ser = Serial('/dev/ttyACM0', 115200)

        time.sleep(1)
        ser.setDTR(level=0)
        time.sleep(1)

        Logger.logEverywhere("ROBOT: rotating of " + str(angleInDegrees) + " degrees")
        ser.write('R' + str(angleInDegrees) + '.')

        self.__checkIfOperationIsOver(ser)

    def __checkIfOperationIsOver(self, ser):

        operationOver = False

        while not operationOver:
            time.sleep(0.1)
            line = ser.readline()
            if line.find("over") != -1:
                operationOver = True