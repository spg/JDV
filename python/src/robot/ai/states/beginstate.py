from python.src.robot.ai.statecontroller import StateController
from python.src.robot.ai.states.searchlocation import SearchLocation
from python.src.robot.ai.states.state import State

class BeginState(State):
    def __init__(self):
        pass

    def run(self):
        print "begin state running..."
        StateController.instance.setCurrentState(SearchLocation())