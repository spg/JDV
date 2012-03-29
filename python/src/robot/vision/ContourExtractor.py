import cv2.cv as cv
import math

class ContourExtractor:
    MIN_CONTOUR_AREA = 40000
    MIN_DISTANCE_BETWEEN_POINTS = 20

    def findContours(self,image):
        tmp = cv.CreateImage(cv.GetSize(image), 8, 1)
        cv.CvtColor(image, tmp, cv.CV_BGR2GRAY)
        cv.Smooth(tmp, tmp, cv.CV_GAUSSIAN, 5, 5)

        size = cv.GetSize(image)
        middleOfSideImage = size[0]/2
        minTreshold = cv.GetReal2D(tmp, middleOfSideImage, middleOfSideImage)

        cv.Threshold(tmp,tmp, minTreshold+20,255,cv.CV_THRESH_BINARY)
        cv.Dilate(tmp, tmp)
        cv.Dilate(tmp, tmp)
        cv.Erode(tmp, tmp)
        cv.Erode(tmp, tmp)

        storage = cv.CreateMemStorage()
        contours = cv.FindContours(tmp,
            storage,cv.CV_RETR_LIST,
            cv.CV_CHAIN_APPROX_SIMPLE)
        storage = cv.CreateMemStorage()
        contours = cv.ApproxPoly (contours,
            storage,
            cv.CV_POLY_APPROX_DP, 3, 1)

        contour = self.findCorrectContour(contours)
        contour = self.removePointClusters(contour)
        contour = self.convertPointsToDrawingPlane(contour, size[0])

        return contour

    def convertPointsToDrawingPlane(self, points, imageSize):
        newPoints = []
        for point in points:
            x = point[0]
            y = imageSize - point[1]
            newPoints.append((x,y))
        return newPoints

    def findCorrectContour(self, contours):
        _contour = contours
        validContours = []
        while _contour is not None:
            if len(_contour) > 4 and cv.ContourArea(_contour) > self.MIN_CONTOUR_AREA:
                validContours.append(_contour)
            _contour = _contour.h_next()

        if len(validContours) > 1:
            drawingContour = validContours[0]
            for contour in validContours:
                if cv.ContourArea(drawingContour) > cv.ContourArea(contour):
                    drawingContour = contour
        else:
            drawingContour = validContours[0]

        return drawingContour

    def removePointClusters(self, points):
        unclusteredPoints = []
        for i in range(len(points)):
            if i == len(points) - 1:
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[0][0]
                y2 = points[0][1]
            else:
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[i+1][0]
                y2 = points[i+1][1]

            distance = math.sqrt(math.pow(y2 - y1, 2) + math.pow(x2 - x1, 2))

            if distance > self.MIN_DISTANCE_BETWEEN_POINTS:
                unclusteredPoints.append(points[i])

        return unclusteredPoints