class ConfirmEvent:
    _handlers = []

    @staticmethod
    def addHandler(handler):
        ConfirmEvent._handlers.append(handler)

    @staticmethod
    def fire(*args, **keywargs):
        for handler in ConfirmEvent._handlers:
            handler(*args, **keywargs)