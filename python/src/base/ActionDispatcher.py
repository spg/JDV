import cPickle
from src.shared.actions import LogMessage

class ActionDispatcher():
    def dispatch(self, msg):
        obj = cPickle.loads(msg)

        if obj.__class__.__name__ == LogMessage.__name__:
            print 'we have a logging message!'