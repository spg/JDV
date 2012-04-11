
import cv2.cv as cv

class ColorSegmenter:
    blue = 0
    orange = 1
    red = 2
    green = 3
    white = 4

    def __init__(self):
        self.lowerTreshold = []
        self.upperTreshold = []

        #Tresholds for the color blue
        self.lowerTreshold.append(cv.Scalar(75, 0,0))
        self.upperTreshold.append(cv.Scalar(140,255,255))

        #Tresholds for the color orange
        self.lowerTreshold.append(cv.Scalar(0,100,100))
        self.upperTreshold.append(cv.Scalar(12,255,255))

        #Tresholds for the color red
        self.lowerTreshold.append(cv.Scalar(0,100,100))
        self.upperTreshold.append(cv.Scalar(4,255,255))

        #Tresholds for the color green
        self.lowerTreshold.append(cv.Scalar(30,100,50))
        self.upperTreshold.append(cv.Scalar(90,255,255))

        #Tresholds for the color white
        self.lowerTreshold.append(cv.Scalar(0,0,250))
        self.upperTreshold.append(cv.Scalar(255,255,255))

    def segmentImageByColor(self, sourceImage, color, nbErode, nbDilate):
        if color >= 0 and color <= 5:
            hsvImage = self.convertImageToHSV(sourceImage)
            imgTresh = cv.CreateImage(cv.GetSize(sourceImage), 8, 1)
            imgTresh = self.treshHSVImageByGivenColor(hsvImage, imgTresh, color)
            imgTresh = self.reduceNoiseOnTreshedImage(imgTresh, nbErode, nbDilate)
            cv.SaveImage("segmentationResult.jpg", imgTresh)
            return imgTresh

    def convertImageToHSV(self, sourceImage):
        hsvImage = cv.CreateImage(cv.GetSize(sourceImage), 8, 3)
        cv.CvtColor(sourceImage, hsvImage, cv.CV_BGR2HSV)
        return hsvImage

    def treshHSVImageByGivenColor(self, hsvImage, imgTresh, color):
        cv.SaveImage("BeforeTresh.jpg", hsvImage)
        cv.InRangeS(hsvImage, self.lowerTreshold[color], self.upperTreshold[color], imgTresh)
        cv.SaveImage("AfterTresh.jpg", imgTresh)
        return imgTresh

    def reduceNoiseOnTreshedImage(self, imgTresh, nbErode, nbDilate):
        cv.Erode(imgTresh, imgTresh, None, nbErode)
        cv.Dilate(imgTresh, imgTresh, None, nbDilate)
        return imgTresh

