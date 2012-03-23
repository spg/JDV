from src.robot.ai.statecontroller import StateController
from src.robot.ai.states.searchlocation import SearchLocation
from src.robot.ai.states.state import State

class BeginState(State):
    def __init__(self):
        pass

    def run(self):
        print "begin state running..."
        StateController.instance.setCurrentState(SearchLocation())