import cPickle
#import serial
from Logger import Logger
from src.shared.actions import startrobot

class ActionDispatcher:
    def __init__(self, robot):
        self._robot = robot

    def dispatch(self, msg):
        obj = cPickle.loads(msg)
        moduleName = obj.__module__

        if moduleName == startrobot.__name__:
            logger = Logger(self._robot)
            logger.log('Robot started')
            #s = serial.Serial('/dev/ttyAMC0', 9600)
            #s.write('V50.')