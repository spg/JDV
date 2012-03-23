class PoseEvent:
    _handlers = []

    @staticmethod
    def addHandler(handler):
        PoseEvent._handlers.append(handler)

    @staticmethod
    def fire(*args, **keywargs):
        for handler in PoseEvent._handlers:
            handler(*args, **keywargs)