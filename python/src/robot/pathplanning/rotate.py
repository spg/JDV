class Rotate:
    def __init__(self, angleInDegrees):
        self.angleInDegrees = angleInDegrees

    def getType(self):
        return "Rotate"

    def __repr__(self):
        return "Rotate: " + str(self.angleInDegrees)