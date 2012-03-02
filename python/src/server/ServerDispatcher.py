import cPickle
import serial
from src.server.actions import StartAction

class ServerDispatcher():
    def dispatch(self, msg):
        obj = cPickle.loads(msg)

        if obj.__class__.__name__ == StartAction.__name__:
            print 'we have a StartAction!'
            s = serial.Serial('/dev/ttyAMC0', 9600)
            s.write('V50.')