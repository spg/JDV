from python.src.robot.ai.statecontroller import StateController
from python.src.robot.ai.states.drawstate import DrawState
from python.src.robot.ai.states.state import State

class CaptureImageState(State):
    def run(self):
        #capture image

        StateController.instance.setCurrentState(DrawState())