class TupleOperations:
    @staticmethod
    def scale(tuple, scaleFactor):
        l = lambda t: (t[0] * scaleFactor, t[1] * scaleFactor)
        return l(tuple)

    @staticmethod
    def move(tuple, deltaX, deltaY):
        l = lambda t: (t[0] + deltaX, t[1] + deltaY)
        return l(tuple)
