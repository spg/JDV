import cPickle
from src.base.logevent import LogEvent
from src.shared.actions.robottobase import log, sendpose

class ActionDispatcher():
    def dispatch(self, msg):
        obj = cPickle.loads(msg)
        moduleName = obj.__module__

        if moduleName == log.__name__:
            LogEvent.fire(obj.message)
        elif moduleName == sendpose.__name__:
            LogEvent.fire('Received pose:')
            LogEvent.fire('x: ' + str(obj.x) + ', y: ' + str(obj.y) + ', theta: ' + str(obj.theta))