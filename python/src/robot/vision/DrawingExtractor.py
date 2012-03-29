import cv2.cv as cv
import cv2
import math
import copy

class DrawingExtractor:
    MAX_SQUARE_AREA = 50000
    SQUARE_SIZE = 500

    def ExtractShape(self, srcImage):
        copyImage = cv.CloneImage(srcImage)
        imageMatrix = self.__convertImageToMatrix__(srcImage)
        contours = self.__findSquaresInImage__(imageMatrix)
        whiteSquare = self.__findSmallestSquare__(contours)
        whiteSquare = self.__orderSquareCorners__(whiteSquare)
        whiteSquare = self.__convertContourToArray__(whiteSquare)
        copyImage = self.__warpImage__(copyImage, whiteSquare)
        return copyImage

    def __convertImageToMatrix__(self, image):
        cv.SaveImage("conversion.jpg", image)
        imageMatrix = cv2.imread("conversion.jpg")
        return imageMatrix

    def __findSquaresInImage__(self, img):
        img = cv2.GaussianBlur(img, (5, 5), 0)
        squares = []
        for gray in cv2.split(img):
            for thrs in xrange(0, 255, 26):
                if thrs == 0:
                    bin = cv2.Canny(gray, 0, 50, apertureSize=5)
                    bin = cv2.dilate(bin, None)
                else:
                    retval, bin = cv2.threshold(gray, thrs, 255, cv2.THRESH_BINARY)

                contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

                for cnt in contours:
                    cnt_len = cv2.arcLength(cnt, True)
                    cnt = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
                    if self.__isContourASquare__(cnt):
                        cnt = cnt.reshape(-1, 2)
                        if not self.__squareIsOnBorder__(cnt, img.shape):
                            squares.append(cnt)
        return squares

    def __isContourASquare__(self, contour):
        return len(contour) == 4 and cv2.contourArea(contour) > self.MAX_SQUARE_AREA and cv2.isContourConvex(contour)

    def __warpImage__(self, image, corners):
        target = [(0,0), (self.SQUARE_SIZE,0), (self.SQUARE_SIZE,self.SQUARE_SIZE), (0, self.SQUARE_SIZE)]
        mat = cv.CreateMat(3, 3, cv.CV_32F)
        cv.GetPerspectiveTransform(corners, target, mat)
        out = cv.CreateMat(self.SQUARE_SIZE, self.SQUARE_SIZE, cv.CV_8UC3)
        cv.WarpPerspective(image, out, mat, cv.CV_INTER_CUBIC)
        return out

    def __convertContourToArray__(self, squareCorners):
        corners = []
        for point in squareCorners:
            corners.append((point[0], point[1]))
        return corners

    def __squareIsOnBorder__(self, points, imageSize):
        imageLenght = imageSize[1]
        imageHeight = imageSize[0]
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

    def __findSmallestSquare__(self, squares):
        minSquare = squares[0]
        for square in squares:
            if square[0][0] < minSquare[0][0] or square[0][1] < minSquare[0][1]:
                minSquare = square
        return minSquare

    def __orderSquareCorners__(self, square):
        ordered = False
        squareCopy = square
        while ordered == False:
            if ((squareCopy[0][0] > squareCopy[1][0])
                and (squareCopy[0][0] > squareCopy[2][0])
                and (squareCopy[0][1] < squareCopy[3][1])
                and (squareCopy[0][1] < squareCopy[2][1])):
                ordered = True
            else:
                tmp = copy.deepcopy(squareCopy[0])
                squareCopy[0] = squareCopy[1]
                squareCopy[1] = squareCopy[2]
                squareCopy[2] = squareCopy[3]
                squareCopy[3] = tmp

        tmp = copy.deepcopy(squareCopy[0])
        squareCopy[0] = squareCopy[1]
        squareCopy[1] = tmp
        tmp = copy.deepcopy(squareCopy[2])
        squareCopy[2] = squareCopy[3]
        squareCopy[3] = tmp

        return squareCopy

    def findContours(self,image):
        tmp = cv.CreateImage(cv.GetSize(image), 8, 1)
        cv.CvtColor(image, tmp, cv.CV_BGR2GRAY)
        cv.Smooth(tmp, tmp, cv.CV_GAUSSIAN, 5, 5)
        cv.SaveImage("tresh2.jpg", tmp)
        minTreshold = cv.GetReal2D(tmp, 250, 250)
        print minTreshold
        cv.Threshold(tmp,tmp, minTreshold+20,255,cv.CV_THRESH_BINARY)
        cv.Dilate(tmp, tmp)
        cv.Dilate(tmp, tmp)
        cv.Erode(tmp, tmp)
        cv.Erode(tmp, tmp)

        cv.SaveImage("tresh.jpg", tmp)
        storage = cv.CreateMemStorage()
        contours = cv.FindContours(tmp, storage,cv.CV_RETR_LIST,cv.CV_CHAIN_APPROX_SIMPLE)
        storage = cv.CreateMemStorage()
        contours = cv.ApproxPoly (contours,
            storage,
            cv.CV_POLY_APPROX_DP, 3, 1)
        _contours = contours

        contour = self.findCorrectContour(contours)
        contour = self.removePointClusters(contour)
        #contour = self.convertPointsToDrawingPlane(contour, 500)
        cv.DrawContours(image, contours, (0,255,0), (255,0,0), 1, 2)
        for point in contour:
            cv.Circle(image, (point[0], point[1]), 3, (0,0,0))
        return image

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
            if len(_contour) > 4 and cv.ContourArea(_contour) > 40000:
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
            if distance > 20:
                unclusteredPoints.append(points[i])

        return unclusteredPoints


