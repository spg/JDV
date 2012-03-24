from serial import Serial
import time

class PositionController:
    def advance(self, distanceInCentimeters):
        ser = Serial('/dev/ttyACM0', 115200)

        time.sleep(1)
        ser.setDTR(level=0)
        time.sleep(1)

        ser.write('D' + str(distanceInCentimeters) + '.')
        ser.write('A0.')
        ser.write('V5.')
        ser.write('M.')

        self.__checkIfOperationIsOver(ser)


    def rotate(self, angleInDegrees):
        inversedAngle = -angleInDegrees #this is because the angles in the python code are positive in counter-clockwise direction,
                                        #whereas angles in the arduino are positive in clockwise direction.

        ser = Serial('/dev/ttyACM0', 115200)

        time.sleep(1)
        ser.setDTR(level=0)
        time.sleep(1)

        ser.write('R' + str(inversedAngle) + '.')

        self.__checkIfOperationIsOver(ser)

    def __checkIfOperationIsOver(self, ser):

        operationOver = False

        while not operationOver:
            time.sleep(0.1)
            line = ser.readline()
            print line
            if str(line) == "over\n":
                operationOver = True

if __name__== '__main__':
    posctrl = PositionController()
    posctrl.advance(10)
    posctrl.rotate(90)