import time
from python.src.robot.ai.states.state import State
from python.src.robot.ai.statecontroller import StateController
from python.src.robot.sendevent import SendEvent
from python.src.shared.actions.robottobase.sendpose import SendPose

class AdvanceState(State):
    def __init__(self, distanceInCentimeters):
        self.__distanceInCentimeters = distanceInCentimeters

    def run(self):
        SendEvent.send(SendPose(100, 50, 0))
        time.sleep(3)
        SendEvent.send(SendPose(200, 70, 30))
        time.sleep(3)
        SendEvent.send(SendPose(200, 70, 90))

        StateController.instance.endMainLoop()

