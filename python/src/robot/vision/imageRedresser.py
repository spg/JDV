import cv2.cv as cv
import cv2
import math
import copy

class ImageRedresser:

    def RedressDrawingPhoto(self, srcImage):

        dest = cv.GetImage(cv.fromarray(srcImage))

        contours = self.find_squares(srcImage)

        whiteSquare = self.findSmallestSquare(contours)
        whiteSquare = self.orderSquareCorners(whiteSquare)

        a = []
        for point in whiteSquare:
            a.append((point[0], point[1]))

        dest = self.warpImage(dest, a)
        tmp = cv.CreateImage(cv.GetSize(dest), 8, 1)
        cv.CvtColor(dest, tmp, cv.CV_BGR2GRAY)

        tmpImage = cv.CreateImage(cv.GetSize(dest), 8, 1)
        tmpImage2 = cv.CreateImage(cv.GetSize(dest), 8, 1)
        points = cv.GoodFeaturesToTrack(tmp,tmpImage,tmpImage2, 100, 0.01, 100, None, 3, 0, 0.04)

        self.drawShapeContour(dest)
        for point in points:
            center = int(point[0]), int(point[1])
            cv.Circle(dest, (center), 4, (0,0,255))
        return dest

    def find_squares(self, img):
        #img = cv2.GaussianBlur(img, (5, 5), 0)
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
                    if len(cnt) == 4 and cv2.contourArea(cnt) > 10000 and cv2.isContourConvex(cnt):
                        cnt = cnt.reshape(-1, 2)
                        if not self.squareIsOnBorder(cnt):
                            squares.append(cnt)
        return squares


    def warpImage(self, image, corners):
        squareSize = self.getLongestSideOfWarpedSquare(corners)
        target = [(0,0), (squareSize,0), (squareSize,squareSize), (0, squareSize)]
        mat = cv.CreateMat(3, 3, cv.CV_32F)
        cv.GetPerspectiveTransform(corners, target, mat)
        out = cv.CreateMat(squareSize - 20, squareSize - 20, cv.CV_8UC3)
        cv.WarpPerspective(image, out, mat, cv.CV_INTER_CUBIC)
        return out

    def getLongestSideOfWarpedSquare(self, corners):
        upSide = self.getSideLength(corners[0], corners[1])
        downSide = self.getSideLength(corners[2], corners[3])
        leftSide = self.getSideLength(corners[0], corners[2])
        rightSide = self.getSideLength(corners[1], corners[3])

        return int(max(leftSide, rightSide))

    def getSideLength(self, point1, point2):
        deltaX = point1[0] - point2[0]
        deltaY = point1[1] - point2[1]
        return math.ceil(math.sqrt(deltaX**2 + deltaY**2))

    def squareIsOnBorder(self, points):
        for point in points:
            if point[0] < 5:
                return True
            if point[1] < 5:
                return True
        return False

    def findSmallestSquare(self, squares):
        minSquare = squares[0]
        for square in squares:
            if square[0][0] < minSquare[0][0] or square[0][1] < minSquare[0][1]:
                minSquare = square
        return minSquare

    def orderSquareCorners(self, square):
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

    def drawShapeContour(self, image):
        gray = cv.CreateImage(cv.GetSize(image), 8, 1)
        cv.CvtColor(image, gray, cv.CV_BGR2GRAY)


        cv.SaveImage("test.jpg", gray)
        #bin = cv.Dilate(gray, None)
        #contours = cv.FindContours(gray, storage, cv.CV_RETR_TREE, cv.CV_CHAIN_APPROX_SIMPLE)

        contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours =  cv.ApproxPoly(contours, storage, cv.CV_POLY_APPROX_DP)
        _contour = contours
        while _contour is not None:
            print _contour
            _contour.h_next()


        for cnt in contours:
            print cnt
            lastContour = cnt

        cv.DrawContours(image, contours, (0,255,0),, (255,0,0), -1, 2)
