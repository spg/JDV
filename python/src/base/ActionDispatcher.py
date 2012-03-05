import cPickle
from src.base.logevent import LogEvent
from src.shared.actions import log

class ActionDispatcher():
    def dispatch(self, msg):
        obj = cPickle.loads(msg)
        moduleName = obj.__module__

        if moduleName == log.__name__:
            LogEvent.fire(obj.message)