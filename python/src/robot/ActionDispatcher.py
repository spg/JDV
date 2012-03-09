import cPickle
#import serial
from Logger import Logger
from src.shared.actions import startrobot
from src.shared.actions.basetorobot import getpose, startrobot
from src.shared.actions.robottobase.sendpose import SendPose

class ActionDispatcher:
    def __init__(self, robot):
        self.__robot = robot
        self.__logger = Logger(robot)

    def dispatch(self, msg):
        obj = cPickle.loads(msg)
        moduleName = obj.__module__

        if moduleName == startrobot.__name__:
            self.__logger.log('Robot started')
            self.__robot.activate()

        elif moduleName == getpose.__name__:
            self.__robot.send(SendPose(2, 4, 120))
