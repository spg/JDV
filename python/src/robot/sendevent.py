import cPickle

class SendEvent:
    _handlers = []

    @staticmethod
    def addHandler(handler):
        SendEvent._handlers.append(handler)

    @staticmethod
    def __fire(*args, **keywargs):
        for handler in SendEvent._handlers:
            handler(*args, **keywargs)

    @staticmethod
    def send(action):
        SendEvent.__fire(cPickle.dumps(action))