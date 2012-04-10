import cv
import numpy

class CameraAccessor:

    def __init__(self):
        self.__initialiseCamera__()
        self.__getCalibrationParameters__()
        self.__initialiseUndistortMap__()

    def getFrame(self):
        frame = cv.QueryFrame(self.camera)
        undistortedFrame = cv.CreateImage(cv.GetSize(frame), 8, 3)

        cv.Remap(frame, undistortedFrame, self.mapx, self.mapy)
        return undistortedFrame

    def __getCalibrationParameters__(self):
        self.intrinsecParameters = numpy.load("vision/intrinsec.npy")
        self.distortionParameter = numpy.load("vision/distortion.npy")

    def __initialiseCamera__(self):
        self.camera = cv.CaptureFromCAM(0)
        cv.SetCaptureProperty(self.camera, cv.CV_CAP_PROP_FRAME_HEIGHT, 1200)
        cv.SetCaptureProperty(self.camera, cv.CV_CAP_PROP_FRAME_WIDTH, 1600)
        print "CameraAccessor: initialiseCamera - set format begin"
        #cv.SetCaptureProperty(self.camera, cv.CV_CAP_PROP_FORMAT, cv.IPL_DEPTH_32F)
        print "CameraAccessor: initialiseCamera - set format end"

    def __initialiseUndistortMap__(self):
        #testImage = cv.QueryFrame(self.camera) 
        #print type(testImage)
        #self.photoSize = cv.GetSize(testImage)
        self.photoSize = (1600, 1200)
        self.mapx = cv.CreateImage(self.photoSize, cv.IPL_DEPTH_32F, 1)
        self.mapy = cv.CreateImage(self.photoSize, cv.IPL_DEPTH_32F, 1)
        cv.InitUndistortMap(cv.fromarray(self.intrinsecParameters), cv.fromarray(self.distortionParameter), self.mapx, self.mapy)

