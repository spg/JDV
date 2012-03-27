import cPickle
from python.src.shared.actions.robottobase import log, sendpose,senddesssin,sendtrajectoire
from python.src.base.logevent import LogEvent
from python.src.base.poseevent import PoseEvent
from python.src.base.trajectoireevent import TrajectoireEvent
from python.src.base.dessinevent import DessinEvent

class ActionDispatcher():
    def dispatch(self, msg):
        obj = cPickle.loads(msg)
        moduleName = obj.__module__

        if moduleName == log.__name__:
            LogEvent.fire("'Received message:'")
            LogEvent.fire(obj.message)
        elif moduleName == sendpose.__name__:
            LogEvent.fire('Received pose:')
            PoseEvent.fire(obj)
        elif moduleName == senddesssin.__name__:
            LogEvent.fire('Received draw:')
            DessinEvent.fire(obj)
        elif moduleName == sendtrajectoire.__name__:
            LogEvent.fire('Received path:')
            TrajectoireEvent.fire(obj)
