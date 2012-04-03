from python.src.robot.util.tuplescaler import TupleOperations

class PointsCloudOperations:
    @staticmethod
    def scale(pointsCloud, scaleFactor):
        scaled = []

        for point in pointsCloud:
            scaled.append(TupleOperations.scale(point, scaleFactor))

        return scaled

    @staticmethod
    def move(pointsCloud, deltaX, deltaY):
        moved = []

        for point in pointsCloud:
            moved.append(TupleOperations.move(point, deltaX, deltaY))

        return moved
