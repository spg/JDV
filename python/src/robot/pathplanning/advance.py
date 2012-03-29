class Advance:
    def __init__(self, distanceInCentimeters):
        self.distanceInCentimeters = distanceInCentimeters

    def getType(self):
        return "Advance"

    def __repr__(self):
        return "Advance: " + str(self.distanceInCentimeters)