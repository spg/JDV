from python.src.robot.arduino.arduinointerface import ArduinoInterface

class PrehensorController:
    def __init__(self):
        self.arduinoInterface = ArduinoInterface.getInstance()

    def dropPrehensor(self):
        self.arduinoInterface.write('PD.')

        self.arduinoInterface.checkIfOperationIsOver()

    def raisePrehensor(self):
        self.arduinoInterface.write('PR.')

        self.arduinoInterface.checkIfOperationIsOver()
