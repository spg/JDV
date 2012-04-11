from __future__ import division
from CornerDetector import CornerDetector
import numpy as np
import math
from python.src.robot.terrain import Terrain

class Positionner:
    def __init__(self):
        transformationMatrix = np.load("vision/extrinsec.npy")
        self.m11 = transformationMatrix[0][0]
        self.m12 = transformationMatrix[0][1]
        self.m13 = transformationMatrix[0][2]
        self.m14 = transformationMatrix[0][3]
        self.m21 = transformationMatrix[1][0]
        self.m22 = transformationMatrix[1][1]
        self.m23 = transformationMatrix[1][2]
        self.m24 = transformationMatrix[1][3]
        self.m31 = transformationMatrix[2][0]
        self.m32 = transformationMatrix[2][1]
        self.m33 = transformationMatrix[2][2]
        self.m34 = transformationMatrix[2][3]
        self.CORNER_LENGHT = 17
        self.TABLE_LENGHT = 229.8
        self.TABLE_HEIGHT = 111

    def getCurrentPose(self, point1, point2, corner):
        cameraPoint1 = self.getPositionRelativeToCamera(point1)
        cameraPoint2 = self.getPositionRelativeToCamera(point2)
        robotPoint1 = self.convertPointToRobotCoordinates(cameraPoint1)
        robotPoint2 = self.convertPointToRobotCoordinates(cameraPoint2)
        defaultAngle = self.getCornerAngle(corner)
        offsetAngle = self.calculateAngleBetweenPoints(robotPoint1, robotPoint2, corner)
        robotAngle = defaultAngle +  offsetAngle
        x,y = self.getRobotPosition(robotPoint1, robotPoint2, corner)
        return x, y, robotAngle

    def getPositionRelativeToCamera(self, point):
        u = point[0]
        v = point[1]
        s = (self.m11 - u*self.m31)*(self.m22 - v*self.m32) + (self.m12 - u*self.m32)*(-self.m21 + v*self.m31)
        X = ((-self.m14 + u*self.m34)*(self.m22 - v*self.m32) - (self.m24 - v*self.m34)*(-self.m12 + u*self.m32)) / s
        Y = ((-self.m14 + u*self.m34)*(-self.m21 + v*self.m31) - (self.m24 - v*self.m34)*(self.m11 - u*self.m31)) / s
        return (X,Y)

    def convertPointToRobotCoordinates(self, point):
        yDistanceFromPicturOrigin = 68.58
        newX = point[0]
        newY = -1*(point[1] - yDistanceFromPicturOrigin)
        return (newX, newY)

    def getRealWorldCoordinates(self, point1, point2, corner):
        if corner == CornerDetector.WEST_BLUE_CORNER:
            rwc1 = Terrain.CORNER_BLUE_WEST_LEFT_EDGE
            rwc2 = Terrain.CORNER_BLUE_WEST_RIGHT_EDGE
        elif corner == CornerDetector.WEST_ORANGE_CORNER:
            rwc1 = Terrain.CORNER_ORANGE_WEST_LEFT_EDGE
            rwc2 = Terrain.CORNER_ORANGE_WEST_RIGHT_EDGE
        elif corner == CornerDetector.EAST_ORANGE_CORNER:
            rwc1 = Terrain.CORNER_ORANGE_EAST_LEFT_EDGE
            rwc2 = Terrain.CORNER_ORANGE_EAST_RIGHT_EDGE
        elif corner == CornerDetector.WEST_BLUE_CORNER:
            rwc1 = Terrain.CORNER_BLUE_EAST_LEFT_EDGE
            rwc2 = Terrain.CORNER_BLUE_EAST_RIGHT_EDGE
        return rwc1, rwc2

    def calculateAngleBetweenPoints(self, point1, point2, corner):
        deltaX = point2[0] - point1[0]
        deltaY = point2[1] - point1[1]
        theta = math.atan(deltaY/deltaX)
        return theta*360/(2* math.pi)

    def getCornerAngle(self, corner):
        if corner == CornerDetector.WEST_BLUE_CORNER:
            return -135
        elif corner == CornerDetector.WEST_ORANGE_CORNER:
            return 135
        elif corner == CornerDetector.EAST_ORANGE_CORNER:
            return 45
        elif corner == CornerDetector.EAST_BLUE_CORNER:
            return -45


    def getDistanceBetweenPoints(self, point1, point2):
        return math.sqrt(math.pow(point2[0]- point1[0], 2) + math.pow(point2[1] - point1[1], 2))

    def getRobotPosition(self, point1, point2, corner):
        sideLeft = self.getDistanceBetweenPoints(point1, (0,0))
        sideRight = self.getDistanceBetweenPoints(point2, (0,0))
        angleLeft, angleRight = self.getAnglesByCosinusLaw(sideLeft, sideRight)
        angleLeft = 180 - 45 - angleLeft
        angleRight = 180 - 45 - angleRight
        leftPosition = math.sin(math.radians(angleLeft))*sideLeft
        rightPosition = math.sin(math.radians(angleRight))*sideRight
        print leftPosition
        print rightPosition
        x = 0
        y = 0
        if corner == CornerDetector.WEST_BLUE_CORNER:
            x = leftPosition
            y = self.TABLE_HEIGHT - rightPosition
        elif corner == CornerDetector.WEST_ORANGE_CORNER:
            x = rightPosition
            y = leftPosition
        elif corner == CornerDetector.EAST_ORANGE_CORNER:
            x = self.TABLE_LENGHT - leftPosition
            y = rightPosition
        elif corner == CornerDetector.EAST_BLUE_CORNER:
            x = self.TABLE_LENGHT - rightPosition
            y = self.TABLE_HEIGHT - leftPosition
        return x, y


    def getAnglesByCosinusLaw(self, sideLeft, sideRight):
        cosRight = (math.pow(sideLeft, 2) - math.pow(sideRight,2) - math.pow(self.CORNER_LENGHT,2)) / (-2*sideRight*self.CORNER_LENGHT)
        angleRight = math.acos(cosRight)
        cosLeft = (math.pow(sideRight, 2) - math.pow(sideLeft,2) - math.pow(self.CORNER_LENGHT,2)) / (-2*sideLeft*self.CORNER_LENGHT)
        angleLeft = math.acos(cosLeft)
        return math.degrees(angleLeft), math.degrees(angleRight)
