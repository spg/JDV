import time
from src.robot.ai.statecontroller import StateController
from src.robot.ai.states.advancestate import AdvanceState
from src.robot.ai.states.state import State
from src.robot.sendevent import SendEvent
from src.shared.actions.robottobase.log import Log

class SearchLocation(State):
    def __init__(self):
        pass

    def run(self):
        print "searching location..."
        SendEvent.send(Log("Searching location..."))
        self.__searchLocation()
        print "location found!..."
        SendEvent.send(Log("Location found!"))
        StateController.instance.setCurrentState(AdvanceState(20))

    def __searchLocation(self):
        time.sleep(3)