from python.src.robot.arduino.arduinointerface import ArduinoInterface

class CaptorsController:
    def __init__(self):
        self.arduinoInterface = ArduinoInterface.getInstance()

    def Zing(self):
        ser = self.arduinoInterface.connect()

        ser.write('Z.')

        self.arduinoInterface.checkIfOperationIsOver(ser)