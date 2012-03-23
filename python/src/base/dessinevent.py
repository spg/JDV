class DessinEvent:
    _handlers = []

    @staticmethod
    def addHandler(handler):
        DessinEvent._handlers.append(handler)

    @staticmethod
    def fire(*args, **keywargs):
        for handler in DessinEvent._handlers:
            handler(*args, **keywargs)