from serial import Serial
import time

class PositionController:
    def advance(self, distanceInCentimeters):
        ser = Serial('/dev/ttyAMC0', 115200)

        time.sleep(1)
        ser.setDTR(level=0)
        time.sleep(1)

        ser.write('D' + distanceInCentimeters + '.')
