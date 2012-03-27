import cPickle
from python.src.robot.ai.statecontroller import StateController
from python.src.robot.ai.states.beginstate import BeginState
from python.src.robot.logger import Logger

from python.src.shared.actions.basetorobot import    startrobot

class ActionDispatcher:
    def dispatch(self, msg):
        obj = cPickle.loads(msg)
        moduleName = obj.__module__

        if moduleName == startrobot.__name__:
            Logger.logToBase('Robot started')

            obstacle1 = (obj.obstacle_1_x, obj.obstacle_1_y)
            obstacle2 = (obj.obstacle_2_x, obj.obstacle_2_y)

            stateController = StateController(BeginState(obstacle1, obstacle2))
            stateController.beginMainLopp()

