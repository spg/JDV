import cPickle
#import serial
from Logger import Logger
from src.shared.actions import startrobot, getpose

class ActionDispatcher:
    def __init__(self, robot):
        self.__robot = robot
        self.__logger = Logger(robot)

    def dispatch(self, msg):
        obj = cPickle.loads(msg)
        moduleName = obj.__module__

        if moduleName == startrobot.__name__:
            self.__logger.log('Robot started')
            #s = serial.Serial('/dev/ttyAMC0', 9600)
            #s.write('V50.')
        elif moduleName == getpose.__name__:
            self.__logger.log('About to send pose: ')
