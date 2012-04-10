import cv2.cv as cv
import cv2
import math
import copy
from ColorSegmenter import ColorSegmenter

cs = ColorSegmenter()

class DrawingExtractor:
    MAX_SQUARE_AREA = 50000
    SQUARE_SIZE = 500

    def ExtractShape(self, srcImage):
        print "Drawing Extractor extractShape begin"
        copyImage = cv.CloneImage(srcImage)
        firstTreshing = cs.segmentImageByColor(srcImage, 3)
        imageMatrix = self.__convertImageToMatrix__(firstTreshing)
        contours = self.__findSquaresInImage__(imageMatrix)
        whiteSquare = self.__findSmallestSquare__(contours)
        whiteSquare = self.__orderSquareCorners__(whiteSquare)
        whiteSquare = self.__convertContourToArray__(whiteSquare)
        copyImage = self.__warpImage__(copyImage, whiteSquare)
        print "Drawing Extractor extractShape end"
        return copyImage

    def __convertImageToMatrix__(self, image):
        print "Drawing Extractor convertImageToMatrix begin"
        cv.SaveImage("conversion.jpg", image)
        imageMatrix = cv2.imread("conversion.jpg")
        print "Drawing Extractor convertImageToMatrix begin"
        return imageMatrix

    def __findSquaresInImage__(self, img):
        print "Drawing Extractor findSquaresInImage begin"
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
        print "Drawing Extractor findSquaresInImage end"
        return squares

    def __isContourASquare__(self, contour):
        print "Drawing Extractor isContouraSquare begin"
        print "Drawing Extractor isContouraSquare end"
        return len(contour) == 4 and cv2.contourArea(contour) > self.MAX_SQUARE_AREA and cv2.isContourConvex(contour)

    def __warpImage__(self, image, corners):
        print "Drawing Extractor warpImage begin"
        target = [(0,0), (self.SQUARE_SIZE,0), (self.SQUARE_SIZE,self.SQUARE_SIZE), (0, self.SQUARE_SIZE)]
        mat = cv.CreateMat(3, 3, cv.CV_32F)
        cv.GetPerspectiveTransform(corners, target, mat)
        out = cv.CreateMat(self.SQUARE_SIZE, self.SQUARE_SIZE, cv.CV_8UC3)
        cv.WarpPerspective(image, out, mat, cv.CV_INTER_CUBIC)
        print "Drawing Extractor warpImage end"
        return out

    def __convertContourToArray__(self, squareCorners):
        print "Drawing Extractor convertContourToArray begin"
        corners = []
        for point in squareCorners:
            corners.append((point[0], point[1]))
        print "Drawing Extractor convertContourToArray end"
        return corners

    def __squareIsOnBorder__(self, points, imageSize):
        print "Drawing Extractor squareIsOnBorder begin"
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
        print "Drawing Extractor squareIsOnBorder end"
        return False

    def __findSmallestSquare__(self, squares):
        print "Drawing Extractor findSmallestSquare begin"
        minSquare = squares[0]
        for square in squares:
            if square[0][0] < minSquare[0][0] or square[0][1] < minSquare[0][1]:
                minSquare = square
        print "Drawing Extractor findSmallestSquare end"
        return minSquare

    def __orderSquareCorners__(self, square):
        print "Drawing Extractor orderSquareCorners begin"
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
        print "Drawing Extractor orderSquareCorners end"
        return squareCopy





