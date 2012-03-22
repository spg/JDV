import cPickle
from src.base.logevent import LogEvent
from src.shared.actions.robottobase import log, sendpose,senddesssin,sendtrajectoire

class ActionDispatcher():
    def dispatch(self, msg):
        obj = cPickle.loads(msg)
        moduleName = obj.__module__

        if moduleName == log.__name__:
            LogEvent.fire("'Received message:'")
            LogEvent.fire(obj.message)
        elif moduleName == sendpose.__name__:
            LogEvent.fire('Received pose:')
            LogEvent.fire(obj)
        elif moduleName == senddesssin.__name__:
            LogEvent.fire('Received lineDes:')
            LogEvent.fire(obj)
        elif moduleName == sendtrajectoire.__name__:
            LogEvent.fire('Received lineTra:')
            LogEvent.fire(obj)
