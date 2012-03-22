class DessinEvent:
    _handlers = []

    @staticmethod
    def addHandler(handler):
        LogEvent._handlers.append(handler)

    @staticmethod
    def fire(*args, **keywargs):
        for handler in LogEvent._handlers:
            handler(*args, **keywargs)