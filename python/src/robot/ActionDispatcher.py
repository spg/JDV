import cPickle
#import serial
from Logger import Logger
#from src.shared.actions import startrobot
from src.shared.actions.basetorobot import getpose,getlinedes, getlinetra, startrobot
from src.shared.actions.robottobase.sendpose import SendPose
from src.shared.actions.robottobase.sendlinedes import SendLineDes
from src.shared.actions.robottobase.sendlinetra import SendLineTra

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
            self.__robot.activate()
            self.x1 = obj.obstacle_1_x
            self.y1 = obj.obstacle_1_y
            self.x2 = obj.obstacle_2_x
            self.y2 = obj.obstacle_2_y
        elif moduleName == getpose.__name__:
            self.__robot.send(SendPose(20, 40, 120))

        elif moduleName == getlinedes.__name__:
            self.y2 = self.y2 + 10
            self.y1 = self.y1 + 10
            self.__robot.send(SendLineDes(20, self.y1, 50,self.y2))
        elif moduleName == getlinetra.__name__:
            self.y2 = self.y2 + 10
            self.y1 = self.y1 + 10
            self.__robot.send(SendLineTra(20, self.y1, 50,self.y2))

