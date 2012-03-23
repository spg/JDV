from python.src.robot.ai.states.state import State
from python.src.robot.ai.statecontroller import StateController
from python.src.robot.arduino.positioncontroller import PositionController

class AdvanceState(State):
    def __init__(self, distanceInCentimeters):
        self.__distanceInCentimeters = distanceInCentimeters

    def run(self):
        positionCtrl = PositionController()
        positionCtrl.advance(10)

        StateController.instance.endMainLoop()

