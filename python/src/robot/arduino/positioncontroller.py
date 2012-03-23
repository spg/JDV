from serial import Serial
import time

class PositionController:
    def advance(self, distanceInCentimeters):
        ser = Serial('/dev/ttyACM0', 115200)

        time.sleep(1)
        ser.setDTR(level=0)
        time.sleep(1)

        ser.write('D' + distanceInCentimeters + '.')
        ser.write('A0.')
        ser.write('V5.')
        ser.write('M.')

if __name__=="__main__":
    positionctrl = PositionController()
    positionctrl.advance(10)