from serial import Serial
import time

class ArduinoInterface:
    def connect(self):
        ser = Serial('/dev/ttyACM0', 115200)

        time.sleep(1)
        ser.setDTR(level=0)
        time.sleep(1)

        return ser

    def checkIfOperationIsOver(self, ser):

        operationOver = False

        while not operationOver:
            time.sleep(0.1)
            line = ser.readline()
            if line.find("over") != -1:
                operationOver = True
