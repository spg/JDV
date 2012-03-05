import cPickle
import serial
from Logger import Logger
from src.shared.actions import StartAction

class ActionDispatcher():
    def dispatch(self, msg):
        obj = cPickle.loads(msg)

        if obj.__class__.__name__ == StartAction.__name__:
            print 'we have a StartAction!'
            Logger.log('Robot started')
            #s = serial.Serial('/dev/ttyAMC0', 9600)
            #s.write('V50.')