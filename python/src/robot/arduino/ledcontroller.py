from python.src.robot.arduino.arduinointerface import ArduinoInterface

class LedController:
    def __init__(self):
        self.arduinoInterface = ArduinoInterface.getInstance()

    def turnLedOn(self):
        self.arduinoInterface.write('L1.')

    def turnLedOff(self):
        self.arduinoInterface.write('L0.')