from cameraAccessor import CameraAccessor
from DrawingExtractor import DrawingExtractor
from ContourExtractor import ContourExtractor
from CornerDetector import CornerDetector
from SideDetector import SideDetector
from Positioner import Positionner
import cv2.cv as cv

class Camera:
    def __init__(self):
        self.camera = CameraAccessor()
        self.drawingExtractor = DrawingExtractor()
        self.contourExtractor = ContourExtractor()
        self.cornerDetector = CornerDetector()
        self.sideDetector = SideDetector()
        self. positionner = Positionner()

    def getDrawingContour(self):
        try:
            image = self.camera.getFrame(False)
            drawingImage = self.drawingExtractor.ExtractShape(image)
            contourPoints = self.contourExtractor.findContours(drawingImage)
            size = cv.GetSize(drawingImage)
            squareSize = size[0]
            newSquareSize = size[0]-(2*19)

            for point in contourPoints:
                pointCopy = (point[0], squareSize - point[1])
                cv.Circle(drawingImage, pointCopy, 5, (0,0,0), 2)

            #cv.SaveImage("segmentationResult.jpg", drawingImage)

            return contourPoints, newSquareSize
        except:
            raise ValueError("Couldn't find drawing in image")

    def getCurrentPose(self):
        try:
            image = self.camera.getFrame(False)
            pointBlue, pointOrange, side = self.getVisibleCorners(image)
            print "blue: ", len(pointBlue)
            print "orange: ", len(pointOrange)
            self.drawPointsOnImage(image, pointBlue)
            self.drawPointsOnImage(image, pointOrange)
            if len(pointBlue) > 0 and side == SideDetector.EAST_SIDE:
                print "Blue East Corner"
                x, y, theta = self.positionner.getCurrentPose(pointBlue[0], pointBlue[1], CornerDetector.EAST_BLUE_CORNER)
            elif len(pointBlue) > 0 and side == SideDetector.WEST_SIDE:
                print "Blue West Corner"
                x, y, theta = self.positionner.getCurrentPose(pointBlue[0], pointBlue[1], CornerDetector.WEST_BLUE_CORNER)
            elif len(pointOrange) > 0 and side == SideDetector.EAST_SIDE:
                print "Orange East Corner"
                x, y, theta = self.positionner.getCurrentPose(pointOrange[0], pointOrange[1], CornerDetector.EAST_ORANGE_CORNER)
            elif len(pointOrange) > 0 and side == SideDetector.WEST_SIDE:
                print "Orange West Corner"
                x, y, theta = self.positionner.getCurrentPose(pointOrange[0], pointOrange[1], CornerDetector.WEST_ORANGE_CORNER)
            else:
                print "No corners detected"
                raise ValueError("No corners detected for positionning")
            if theta < 0:
                theta = 360 + theta
            return x, y, theta
        except:
            raise ValueError("Problem while getting robot pose")

    def getCurrentPose2(self):
        xTotal = 0
        yTotal = 0
        thetaTotal = 0
        nbSuccess = 0
        attemps = 0
        try:
            while attemps < 10  and nbSuccess <= 3:
                attemps += 1
                print "Camera: Getting current pose. Attemp ", attemps
                x = 0
                y  = 0
                theta = 0
                image = self.camera.getFrame(False)
                pointBlue, pointOrange, side = self.getVisibleCorners(image)
                #self.drawPointsOnImage(image, pointBlue)
                #self.drawPointsOnImage(image, pointOrange)
                if len(pointBlue) > 0 and side == SideDetector.EAST_SIDE:
                    x, y, theta = self.positionner.getCurrentPose(pointBlue[0], pointBlue[1], CornerDetector.EAST_BLUE_CORNER)
                    print "Camera Getting current pose. Success! Blue East corner found."
                elif len(pointBlue) > 0 and side == SideDetector.WEST_SIDE:
                    x, y, theta = self.positionner.getCurrentPose(pointBlue[0], pointBlue[1], CornerDetector.WEST_BLUE_CORNER)
                    print "Camera Getting current pose. Success! Blue West corner found."
                elif len(pointOrange) > 0 and side == SideDetector.EAST_SIDE:
                    x, y, theta = self.positionner.getCurrentPose(pointOrange[0], pointOrange[1], CornerDetector.EAST_ORANGE_CORNER)
                    print "Camera Getting current pose. Success! Orange East corner found."
                elif len(pointOrange) > 0 and side == SideDetector.WEST_SIDE:
                    x, y, theta = self.positionner.getCurrentPose(pointOrange[0], pointOrange[1], CornerDetector.WEST_ORANGE_CORNER)
                    print "Camera Getting current pose. Success! Orange West corner found."
                if x > 130:
                    nbSuccess += 1
                    xTotal += x
                    yTotal += y
                    thetaTotal += theta
            if nbSuccess > 0:
                xAverage = xTotal/nbSuccess
                yAverage = yTotal/nbSuccess
                thetaAverage = thetaTotal/nbSuccess
                print "Camera: Robot pose found. X = ", xAverage, ", Y = ", yAverage, ", Theta = ", thetaAverage
                return xAverage, yAverage, thetaAverage
            else:
                raise ValueError("Couldn't find corner")
        except:
            raise ValueError("Problem while getting robot pose")

    def getCurrentPoseBackup(self):
        image = self.camera.getFrame(True)
        imageSize = cv.GetSize(image)
        pointBlue, pointOrange, side = self.getVisibleCorners(image)
        if side == SideDetector.EAST_SIDE and len(pointBlue) > 0:
            lenght = (pointBlue[1][0] - pointBlue[0][0])/size[0]
            distance = 1699.1*lenght*lenght - 1051.6*lenght + 229.33
            return True, distance
        else:
            return False, 0

    def drawPointsOnImage(self, image, points):
        #cv.SaveImage("cornerDetectionResult.jpg", image)
        if len(points) > 0:
            for point in points:
                #pointCopy = (point[0], squareSize - point[1])
                cv.Circle(image, point, 5, (0,0,0), 2)
            #cv.SaveImage("cornerDetectionResult.jpg", image)

    def getVisibleCorners(self, image):
        contourBlue, contourOrange = self.cornerDetector.detectCorners(image)
        side = self.sideDetector.detectVisibleSide(image)
        return contourBlue, contourOrange, side


    def __doubleImage__(self, contourPoints, size):
        doubleImage = cv.CreateImage((1000,1000),8,1)
        for scale in range(1,3):
            x = size[0]*scale
            y = size[1]*scale
            for i in range(len(contourPoints)):
                if i == len(contourPoints)-1:
                    x1 = contourPoints[i][0]*scale
                    y1 = contourPoints[i][1]*scale
                    x2 = contourPoints[0][0]*scale
                    y2 = contourPoints[0][1]*scale
                else:
                    x1 = contourPoints[i][0]*scale
                    y1 = contourPoints[i][1]*scale
                    x2 = contourPoints[i+1][0]*scale
                    y2 = contourPoints[i+1][1]*scale
                point1 = (x1, y1)
                point2 = (x2, y2)
                cv.Line(doubleImage,point1, point2,255, 2)

        #cv.SaveImage("scale.jpg", doubleImage)