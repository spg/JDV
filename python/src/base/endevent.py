class EndEvent:
    _handlers = []

    @staticmethod
    def addHandler(handler):
        EndEvent._handlers.append(handler)

    @staticmethod
    def fire(*args, **keywargs):
        for handler in EndEvent._handlers:
            handler(*args, **keywargs)