class TrajectoireEvent:
    _handlers = []

    @staticmethod
    def addHandler(handler):
        TrajectoireEvent._handlers.append(handler)

    @staticmethod
    def fire(*args, **keywargs):
        for handler in TrajectoireEvent._handlers:
            handler(*args, **keywargs)