from python.src.robot.arduino.arduinointerface import ArduinoInterface

class CaptorsController:
    def __init__(self):
        self.arduinoInterface = ArduinoInterface.getInstance()

    def Zing(self):
        self.arduinoInterface.write('Z.')

        self.arduinoInterface.checkIfOperationIsOver()

    def Zing_a(self):
        self.arduinoInterface.write('ZA.')

        self.arduinoInterface.checkIfOperationIsOver()

    def Zing_b(self):
        def Zing_a(self):
            self.arduinoInterface.write('ZB.')

            self.arduinoInterface.checkIfOperationIsOver()