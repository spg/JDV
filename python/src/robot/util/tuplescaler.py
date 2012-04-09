class TupleOperations:
    @staticmethod
    def scale(tuple, scaleFactor):
        l = lambda t: (t[0] * scaleFactor, t[1] * scaleFactor)
        return l(tuple)

    @staticmethod
    def move(tuple, deltaX, deltaY):
        l = lambda t: (t[0] + deltaX, t[1] + deltaY)
        return l(tuple)

    @staticmethod
    def rotate(tuple, theta):
        a = 0
        b = 0
        c = 0
        d = 0

        if theta == 90:
            b = 1
            c = -1
        elif theta == 180:
            a = -1
            d = -1
        elif theta == 270:
            b = -1
            c = 1
        else:
            return tuple

        l = lambda t: (t[0] * a + t[1] * b, t[0] * c + t[1] * d)
        return l(tuple)
