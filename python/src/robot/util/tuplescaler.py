class TupleScaler:
    @staticmethod
    def scaleTuple(tuple, scaleFactor):
        l = lambda t : (t[0]*scaleFactor, t[1]*scaleFactor)
        return l(tuple)
