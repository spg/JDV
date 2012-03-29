from python.src.robot.util.tuplescaler import TupleScaler

class PointsCloudScaler:
    @staticmethod
    def scalePointsCloud(pointsCloud, scaleFactor):
        scaled = []

        for point in pointsCloud:
            scaled.append(TupleScaler.scaleTuple(point, scaleFactor))

        return scaled
