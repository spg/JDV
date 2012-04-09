from __future__ import division
from python.src.robot.arduino.manchestersignalinterpreter import ManchesterSignalInterpreter

from python.src.robot.util.pointscloudscaler import PointsCloudOperations

class ImagePointsTransformer:
    def transform(self, pointsFromImage, orientation, scale):
        transformedPoints = PointsCloudOperations.scale(pointsFromImage[0], 60 / pointsFromImage[1])

        movedPoints = PointsCloudOperations.move(transformedPoints, -30, -30)

        if orientation == ManchesterSignalInterpreter.EAST:
            rotatedPoints = PointsCloudOperations.rotate(movedPoints, 90)
        elif orientation == ManchesterSignalInterpreter.WEST:
            rotatedPoints = PointsCloudOperations.rotate(movedPoints, 270)
        elif orientation == ManchesterSignalInterpreter.SOUTH:
            rotatedPoints = PointsCloudOperations.rotate(movedPoints, 180)
        else:
            rotatedPoints = PointsCloudOperations.rotate(movedPoints, 0)

        if scale == ManchesterSignalInterpreter.FACTOR_2:
            rotatedPoints = PointsCloudOperations.scale(rotatedPoints, 0.5)
            transformedPoints = PointsCloudOperations.move(rotatedPoints, 30, 30)
        else:
            transformedPoints = PointsCloudOperations.move(rotatedPoints, 30, 30)

        return transformedPoints