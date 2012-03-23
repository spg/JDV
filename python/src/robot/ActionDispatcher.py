import cPickle
from Logger import Logger
from python.src.robot.ai.statecontroller import StateController
from python.src.robot.ai.states.beginstate import BeginState
from python.src.shared.actions.basetorobot import    startrobot

class ActionDispatcher:
    def __init__(self, robot):
        self.__robot = robot
        self.__logger = Logger(robot)
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

    def dispatch(self, msg):
        obj = cPickle.loads(msg)
        moduleName = obj.__module__

        if moduleName == startrobot.__name__:
            self.__logger.log('Robot started')
            stateController = StateController(BeginState())
            stateController.beginMainLopp()
            self.x1 = obj.obstacle_1_x
            self.y1 = obj.obstacle_1_y
            self.x2 = obj.obstacle_2_x
            self.y2 = obj.obstacle_2_y

