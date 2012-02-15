from actions.StartAction import StartAction
import cPickle

class ServerDispatcher():
    def dispatch(self, msg):
        obj = cPickle.loads(msg)

        if obj.__class__.__name__ == StartAction.__name__:
            print 'we have a StartAction!'