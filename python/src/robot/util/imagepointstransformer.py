from __future__ import division

from python.src.robot.util.pointscloudscaler import PointsCloudOperations

class ImagePointsTransformer:
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    SCALE_4 = 4
    SCALE_2 = 5

    def __init__(self):
        pass

    def transform(self, pointsFromImage, orientation, scale):
        transformedPoints = PointsCloudOperations.scale(pointsFromImage[0], 60 / pointsFromImage[1])

        movedPoints = PointsCloudOperations.move(transformedPoints, -30, -30)

        if orientation == ImagePointsTransformer.EAST:
            rotatedPoints = PointsCloudOperations.rotate(movedPoints, 90)
        elif orientation == ImagePointsTransformer.WEST:
            rotatedPoints = PointsCloudOperations.rotate(movedPoints, 270)
        elif orientation == ImagePointsTransformer.SOUTH:
            rotatedPoints = PointsCloudOperations.rotate(movedPoints, 180)
        else:
            rotatedPoints = PointsCloudOperations.rotate(movedPoints, 0)

        if scale == ImagePointsTransformer.SCALE_2:
            rotatedPoints = PointsCloudOperations.scale(rotatedPoints, 0.5)
            transformedPoints = PointsCloudOperations.move(rotatedPoints, 30, 30)
        else:
            transformedPoints = PointsCloudOperations.move(rotatedPoints, 30, 30)

        return transformedPoints