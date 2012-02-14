
import cv

class ColorSegmenter:
    blue = 1
    orange = 2
    red = 3
    green = 4
    black = 5
    white = 6

    def __init__(self):
        self.lowerTreshold = []
        self.upperTreshold = []

        #Tresholds for the color blue
        self.lowerTreshold.append(cv.Scalar(105,100,100))
        self.upperTreshold.append(cv.Scalar(1120,255,255))

        #Tresholds for the color orange
        self.lowerTreshold.append(cv.Scalar(105,100,100))
        self.upperTreshold.append(cv.Scalar(1120,255,255))

        #Tresholds for the color red
        self.lowerTreshold.append(cv.Scalar(105,100,100))
        self.upperTreshold.append(cv.Scalar(1120,255,255))

        #Tresholds for the color green
        self.lowerTreshold.append(cv.Scalar(105,100,100))
        self.upperTreshold.append(cv.Scalar(1120,255,255))

        #Tresholds for the color black
        self.lowerTreshold.append(cv.Scalar(105,100,100))
        self.upperTreshold.append(cv.Scalar(1120,255,255))

        #Tresholds for the color white
        self.lowerTreshold.append(cv.Scalar(105,100,100))
        self.upperTreshold.append(cv.Scalar(1120,255,255))

    def segmentImageByColor(self, srcImage, color):
        if color >= 0 and color <= 5:
            #Convert srcImage to HSV color space
            hsvImage = cv.CreateImage(cv.GetSize(srcImage), 8, 3)
            cv.CvtColor(srcImage, hsvImage, cv.CV_BGR2HSV)

            #Create new image to store treshed image
            imgTresh = cv.CreateImage(cv.GetSize(srcImage), 8, 1)

            #Tresh image with chosen color
            cv.InRangeS(hsvImage, self.lowerTreshold[color], self.upperTreshold[color], imgTresh)

            #Reduce the noise in the treshed image by dilating then eroding
            cv.Dilate(imgTresh, imgTresh, None, 1)
            cv.Erode(imgTresh, imgTresh, None, 1)

            return imgTresh
