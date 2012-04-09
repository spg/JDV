import cPickle
from python.src.robot.ai.statecontroller import StateController
from python.src.robot.ai.states.beginstate import BeginState
from python.src.robot.logger import Logger

from python.src.shared.actions.basetorobot import startrobot
from python.src.shared.actions.basetorobot import newturn

class ActionDispatcher:
    def dispatch(self, msg):
        obj = cPickle.loads(msg)
        moduleName = obj.__module__

        if moduleName == startrobot.__name__:
            Logger.logToBase('Robot started')

            obstacle1 = (obj.obstacle_1_x, obj.obstacle_1_y)
            obstacle2 = (obj.obstacle_2_x, obj.obstacle_2_y)

            self.stateController = StateController(BeginState(obstacle1, obstacle2))
            self.stateController.beginMainLopp()
        elif moduleName == newturn.__name__:
            print "beginning a new turn..."
            Logger.logToBase('Beginning a new turn')

            self.stateController.beginMainLopp()

