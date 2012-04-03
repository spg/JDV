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

    def __initialiseUndistortMap__(self):
        self.photoSize = cv.GetSize(cv.QueryFrame(self.camera))
        self.mapx = cv.CreateImage(self.photoSize, cv.IPL_DEPTH_32F, 1)
        self.mapy = cv.CreateImage(self.photoSize, cv.IPL_DEPTH_32F, 1)
        cv.InitUndistortMap(cv.fromarray(self.intrinsecParameters), cv.fromarray(self.distortionParameter), self.mapx, self.mapy)