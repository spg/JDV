from src.robot.ai.state import State
from src.robot.ai.statecontroller import StateController

class AdvanceState(State):
    def __init__(self):
        self.__count = 0

    def run(self):
        self.__count += 1
        if self.__count == 300:
            StateController.instance.endMainLoop()

