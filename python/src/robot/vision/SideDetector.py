from ColorSegmenter import ColorSegmenter
import cv2.cv as cv

class SideDetector:
    WEST_SIDE = 0
    EAST_SIDE = 1
        
    def detectVisibleSide(self, image):
        print "sideDetector - detectVisibleSide begin"
        imageCopy = cv.CloneImage(image)
        colorSegmenter = ColorSegmenter()
        greenSegmentation = colorSegmenter.segmentImageByColor(imageCopy, colorSegmenter.green, 3, 4)
        contours = self.__findContoursInPicture__(greenSegmentation)
        middleHeight = self.__getMiddleHeightOfImage__(imageCopy)
        contours = self.__removeContoursOnBottom__(contours, middleHeight)
        print "sideDetector - detectVisibleSide end"
        if len(contours) > 0:
            return self.WEST_SIDE
        else:
            return self.EAST_SIDE

    def __findContoursInPicture__(self, binaryImage):
        print "sideDetector - findContoursInPicture begin"
        storage = cv.CreateMemStorage()
        contours = cv.FindContours(binaryImage,
            storage,cv.CV_RETR_LIST,
            cv.CV_CHAIN_APPROX_SIMPLE)
        storage = cv.CreateMemStorage()
        if len(contours) > 0:
            contours = cv.ApproxPoly (contours,
                storage,
                cv.CV_POLY_APPROX_DP, 3, 1)
        print "sideDetector - findContoursInPicture end"
        return contours
    
    def __getMiddleHeightOfImage__(self, image):
        size = cv.GetSize(image)
        return size[1]/2
    
    def __removeContoursOnBottom__(self, contours, middleHeight):
        print "sideDetector - removeContoursOnBottom begin"
        filteredContours = []
        _contour = contours
        while _contour is not None:
            nbPoints = 0
            if len(_contour) > 0:
                for point in _contour:
                    if point[1] < middleHeight:
                        nbPoints += 1
                if nbPoints > 0 and cv.ContourArea(_contour) > 1000:
                    filteredContours.append(_contour)
                _contour = _contour.h_next()
            else:
                _contour = None
        print "sideDetector - removeContoursOnBottom end"
        return filteredContours