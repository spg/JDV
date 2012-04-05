class Shuffle:
    def __init__(self, distanceInCentimeters, relativeAngleInDegrees):
        self.distanceInCentimeters = distanceInCentimeters
        self.relativeAngleInDegrees = relativeAngleInDegrees

    def __repr__(self):
        return "Shuffle: " + str(self.distanceInCentimeters) + " cm, " + str(self.relativeAngleInDegrees) + " deg"