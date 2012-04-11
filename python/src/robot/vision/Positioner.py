from __future__ import division
from CornerDetector import CornerDetector
import numpy as np
import math
from python.src.robot.terrain import Terrain

class Positionner:
    def __init__(self):
        print "Positionner - init begin"
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
        print "Positionner - init end"

    def getCurrentPose(self, point1, point2, corner):
        print "Positionner - get current pose begin"
        cameraPoint1 = self.getPositionRelativeToCamera(point1)
        cameraPoint2 = self.getPositionRelativeToCamera(point2)
        print "camera points : ", cameraPoint1, cameraPoint2
        robotPoint1 = self.convertPointToRobotCoordinates(cameraPoint1)
        robotPoint2 = self.convertPointToRobotCoordinates(cameraPoint2)
        print "robot points = ", robotPoint1, robotPoint2
        defaultAngle = self.getCornerAngle(corner)
        print "default angle :  ", defaultAngle
        offsetAngle = self.calculateAngleBetweenPoints(robotPoint1, robotPoint2, corner)
        print "offset angle : ", offsetAngle
        robotAngle = defaultAngle +  offsetAngle
        x,y = self.getRobotPosition(robotPoint1, robotPoint2, corner)
        print "Positionner - get current pose end"
        return x, y, robotAngle

    def getPositionRelativeToCamera(self, point):
        print "Positionner - getPositionRelativeToCam begin"
        u = point[0]
        v = point[1]
        s = (self.m11 - u*self.m31)*(self.m22 - v*self.m32) + (self.m12 - u*self.m32)*(-self.m21 + v*self.m31)
        X = ((-self.m14 + u*self.m34)*(self.m22 - v*self.m32) - (self.m24 - v*self.m34)*(-self.m12 + u*self.m32)) / s
        Y = ((-self.m14 + u*self.m34)*(-self.m21 + v*self.m31) - (self.m24 - v*self.m34)*(self.m11 - u*self.m31)) / s
        print "Positionner - getPositionRelativeToCam end"
        return (X,Y)

    def convertPointToRobotCoordinates(self, point):
        print "Positionner - robotCoord begin"
        yDistanceFromPicturOrigin = 68.58
        newX = point[0]
        newY = -1*(point[1] - yDistanceFromPicturOrigin)
        print "Positionner - robotCoord end"
        return (newX, newY)

    def getRealWorldCoordinates(self, point1, point2, corner):
        print "Positionner - rwc begin"
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
        print "Positionner - rwc end"
        return rwc1, rwc2

    def calculateAngleBetweenPoints(self, point1, point2, corner):
        print "Positionner - calculateangleBetweenPoints begin"
        deltaX = point2[0] - point1[0]
        deltaY = point2[1] - point1[1]
        theta = math.atan(deltaY/deltaX)
        print "Positionner - calculateangleBetweenPoints end"
        return theta*360/(2* math.pi)

    def getCornerAngle(self, corner):
        print "Positionner - getCornerAngle begin"
        if corner == CornerDetector.WEST_BLUE_CORNER:
            return -135
        elif corner == CornerDetector.WEST_ORANGE_CORNER:
            return 135
        elif corner == CornerDetector.EAST_ORANGE_CORNER:
            return 45
        elif corner == CornerDetector.EAST_BLUE_CORNER:
            return -45
        print "Positionner - getCornerAngle end"


    def getDistanceBetweenPoints(self, point1, point2):
        print "Positionner - getDistanceBetweenPoints begin"
        print "Positionner - getDistanceBetweenPoints end"
        return math.sqrt(math.pow(point2[0]- point1[0], 2) + math.pow(point2[1] - point1[1], 2))

    def getRobotPosition(self, point1, point2, corner):
        print "Positionner - getRobotPosition begin"
        sideLeft = self.getDistanceBetweenPoints(point1, (0,0))
        sideRight = self.getDistanceBetweenPoints(point2, (0,0))
        angleLeft, angleRight = self.getAnglesByCosinusLaw(sideLeft, sideRight)
        print "angles : ", angleLeft, angleRight
        angleLeft = 180 - 45 - angleLeft
        angleRight = 180 - 45 - angleRight
        print "angles : ", angleLeft, angleRight
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
        print "Positionner - getRobotPosition end"
        return x, y


    def getAnglesByCosinusLaw(self, sideLeft, sideRight):
        print "Positionner - cosLaw begin"
        cosRight = (math.pow(sideLeft, 2) - math.pow(sideRight,2) - math.pow(self.CORNER_LENGHT,2)) / (-2*sideRight*self.CORNER_LENGHT)
        angleRight = math.acos(cosRight)
        cosLeft = (math.pow(sideRight, 2) - math.pow(sideLeft,2) - math.pow(self.CORNER_LENGHT,2)) / (-2*sideLeft*self.CORNER_LENGHT)
        angleLeft = math.acos(cosLeft)
        print "Positionner - cosLaw end"
        return math.degrees(angleLeft), math.degrees(angleRight)
