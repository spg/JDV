from serial import Serial

ser = Serial('COM3',9600,timeout=.2)
ser.write('A')
ser.close()



class PositionController:
    def advance(self, distanceInCentimeters):
        pass
