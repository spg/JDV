from __future__ import division
import cv2.cv as cv
import math

from ColorSegmenter import ColorSegmenter

class CornerDetector:
    colorSegmenter = ColorSegmenter()
    MIN_CORNER_AREA = 4000
    WEST_BLUE_CORNER = 0
    EAST_BLUE_CORNER = 1
    WEST_ORANGE_CORNER = 2
    EAST_ORANGE_CORNER = 3
    
    def detectCorners(self, srcImage):
        self.imageSize = cv.GetSize(srcImage)
        imageCopy = cv.CloneImage(srcImage)
        cv.Smooth(imageCopy, imageCopy, cv.CV_GAUSSIAN, 5, 5)
        self.__getCenterOfPicture__(imageCopy)

        blueCorner = self.__findColoredCorner__(imageCopy, self.colorSegmenter.blue)
        blueCornerFloorPoints = []
        if len(blueCorner) > 0:
            blueCornerFloorPoints = self.__isolateCornerFloorPoints__(blueCorner)

        orangeCorner = self.__findColoredCorner__(imageCopy, self.colorSegmenter.orange)
        orangeCornerFloorPoints = []
        if len(orangeCorner) > 0:
            orangeCornerFloorPoints = self.__isolateCornerFloorPoints__(orangeCorner)
        return blueCornerFloorPoints, orangeCornerFloorPoints
    
    def __findColoredCorner__(self, image, color):
        contour = []
        segmentedImage = self.colorSegmenter.segmentImageByColor(image, color, 3, 4)
        cv.SaveImage("cornerSegmentation.jpg", segmentedImage)
        contours = self.__findContoursInPicture__(segmentedImage)
        if len(contours) > 0:
            contour = self.__isolateCornerContour__(contours)
            if len(contour) > 0:
                contour = self.__removePointClusters__(contour)
                contour = self.__removeNonCornerPoints__(contour)
        return contour

    def __getCenterOfPicture__(self, image):
        size = cv.GetSize(image)
        xLenght = size[0]
        if xLenght%2 == 0:
            self.xCenter = xLenght/2
        else:
            self.xCenter = (xLenght + 1)/2

        yLenght = size[1]
        if yLenght%2 == 0:
            self.yCenter = yLenght/2
        else:
            self.yCenter = (yLenght + 1)/2
        

    def __findContoursInPicture__(self, binaryImage):
        storage = cv.CreateMemStorage()
        contours = cv.FindContours(binaryImage,
            storage,cv.CV_RETR_LIST,
            cv.CV_CHAIN_APPROX_SIMPLE)
        storage = cv.CreateMemStorage()
        if len(contours) > 0:
            contours = cv.ApproxPoly (contours,
                storage,
                cv.CV_POLY_APPROX_DP, 3, 1)
        return contours

    def __isolateCornerContour__(self, contours):
        _contour = contours
        validContours = []
        while _contour is not None:
            if self.__isContourValid__(_contour):
                validContours.append(_contour)
            _contour = _contour.h_next()
        
        if len(validContours) > 1:
            return self.__findContourWithBiggestArea__(validContours)
        elif len(validContours) == 0:
            return []
        else:
            return validContours[0]
                

    def __isContourValid__(self, contour):
        if len(contour) < 4:
            return False
        if len(contour) > 30:
            return False
        if self.__squareIsOnBorder__(contour):
            return False
        if not self.__isContourOnBottomOfPicture__(contour):
            return False
        if cv.ContourArea(contour) < self.MIN_CORNER_AREA:
            return False
        return True

    def __isContourOnBottomOfPicture__(self, contour):
        cornersOnTopHalf = 0
        for point in contour:
            if point[1] < self.yCenter*0.5:
                print point[1], " ", cornersOnTopHalf
                cornersOnTopHalf += 1
        return cornersOnTopHalf <= 0
    
    def __findContourWithBiggestArea__(self, contours):
        biggestContour = contours[0]
        biggestArea = cv.ContourArea(biggestContour)
        for contour in contours:
            currentArea = cv.ContourArea(contour)
            if currentArea > biggestArea:
                biggestArea = currentArea
                biggestContour = contour

        return biggestContour
    
    def __removePointClusters__(self, contour):
        minDistance = 15
        nbPoints = len(contour)
        filteredContour = []
        i = 0
        while i < nbPoints - 1:
            point1 = contour[i]
            point2 = contour[i+1]
            distance = math.sqrt(math.pow(point1[0] - point2[0],2) + math.pow(point1[1] - point2[1],2))  
            
            if i == 0:
                point3 = contour[nbPoints - 1]
                distance2 = math.sqrt(math.pow(point1[0] - point3[0],2) + math.pow(point1[1] - point3[1],2))
                if distance < minDistance and distance2 < minDistance:
                    filteredContour.append(point1)
                elif distance < minDistance:
                    filteredContour.append(point3)
                    newPoint = (abs(point1[0] + point2[0])//2, abs(point1[1] + point2[1])//2)
                    filteredContour.append(newPoint)
                    i = i + 1
                elif distance2 < minDistance:
                    newPoint = (abs(point1[0] + point3[0])//2, abs(point3[1] + point3[1])//2)
                    filteredContour.append(newPoint)
                else:
                    filteredContour.append(point3)
                    filteredContour.append(point1)
                i = i + 1
            else:
                if distance < minDistance and i < nbPoints - 1:
                    newPoint = (abs(point1[0] + point2[0])//2, abs(point1[1] + point2[1])//2)
                    i = i + 1
                    filteredContour.append(newPoint)
                else:
                    filteredContour.append(point1)
                i = i + 1
        return filteredContour
    
    def __removeNonCornerPoints__(self, contour):
        minDistanbce = 10
        nbPoints = len(contour)
        filteredContour = []
        i = 0
        while i < nbPoints:
            testedPoint = contour[i]
            if i == 0:
                previousPoint = contour[nbPoints - 1]
            else:
                previousPoint = contour[i - 1]
                
            if i == nbPoints - 1:
                nextPoint = contour[0]
            else:
                nextPoint = contour[i+1]
            deltaX = nextPoint[0] - previousPoint[0]
            deltaY = nextPoint[1] - previousPoint[1]
            if deltaX <> 0:
                a = deltaY/deltaX
                b = nextPoint[1] - a* nextPoint[0]

                estimatedHeight = a * testedPoint[0] + b
                realHeight = testedPoint[1]

                if abs(realHeight - estimatedHeight) > minDistanbce:
                    filteredContour.append(testedPoint)

            i += 1
        
        return filteredContour

    def __squareIsOnBorder__(self, points):
        imageLenght = self.imageSize[0]
        imageHeight = self.imageSize[1]
        for point in points:
            if point[0] < 5:
                return True
            if point[0] > imageLenght - 5:
                return True
            if point[1] < 5:
                return True
            if point[1] > imageHeight - 5:
                return True
        return False

    def __isolateCornerFloorPoints__(self, contour):
        lowestLeft = contour[0]
        lowestRight = contour[1]
        for i in range(2, len(contour)):
            if contour[i][1] > lowestLeft[1] and contour[i][1] <= lowestRight[1] and abs(lowestRight[0] - contour[i][0]) > 30:
                lowestLeft = contour[i]
            elif contour[i][1] <= lowestLeft[1] and contour[i][1] > lowestRight[1] and abs(lowestLeft[0] - contour[i][0]) > 30:
                lowestRight = contour[i]
            elif contour[i][1] > lowestLeft[1] and contour[i][1] > lowestRight[1]:
                if lowestLeft[1] > lowestRight[1]:
                    lowestRight = contour[i]
                else:
                    lowestLeft = contour[i]

        if lowestLeft[0] > lowestRight[0]:
            tmp = lowestLeft
            lowestLeft = lowestRight
            lowestRight = tmp
        return [lowestLeft, lowestRight]