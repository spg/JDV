from python.src.robot.arduino.arduinointerface import ArduinoInterface

class PrehensorController:
    def __init__(self):
        self.arduinoInterface = ArduinoInterface.getInstance()

    def dropPrehensor(self):
        ser = self.arduinoInterface.connect()

        self.arduinoInterface.write(ser, 'PD.')

        self.arduinoInterface.checkIfOperationIsOver(ser)

    def raisePrehensor(self):
        ser = self.arduinoInterface.connect()

        self.arduinoInterface.write(ser, 'PR.')

        self.arduinoInterface.checkIfOperationIsOver(ser)
