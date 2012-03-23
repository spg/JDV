from python.src.robot.ai.states.state import State
from python.src.robot.ai.statecontroller import StateController

class AdvanceState(State):
    def __init__(self, distanceInCentimeters):
        self.__distanceInCentimeters = distanceInCentimeters

    def run(self):
        StateController.instance.endMainLoop()

