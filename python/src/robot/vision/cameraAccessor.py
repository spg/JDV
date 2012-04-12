import cv
import numpy

class CameraAccessor:

    def __init__(self):
        #print "CameraAccessor - initialiseCamera begin"
        self.__initialiseCamera__()
        self.__getCalibrationParameters__()
        #self.__initialiseUndistortMap__()
        #print "CameraAccessor - initialiseCamera end"

    def getFrame(self, undistort):
        #self.camera = cv.CaptureFromCAM(-1)
        print "CameraAccessor: Allocating Camera"
        for i in range(1,5):
            frame = cv.QueryFrame(self.camera)
        if undistort == True:
            cv.Remap(frame, frame, self.mapx, self.mapy)
        #cv.ReleaseCapture(self.camera)
        print "CameraAccessor: Releasing camera"
        return frame

    def __getCalibrationParameters__(self):
        self.intrinsecParameters = numpy.load("vision/intrinsec.npy")
        self.distortionParameter = numpy.load("vision/distortion.npy")

    def __initialiseCamera__(self):
        #print "Initialising camera..."
        self.camera = cv.CaptureFromCAM(-1)
        #frame = self.getFrame(False)
        #print "Frame size = ", cv.GetSize(frame)

    def __initialiseUndistortMap__(self):
        #print "CameraAccessor - initialiseUndistortMap begin"
        testImage = cv.QueryFrame(self.camera) 
        #print "imageType = ", type(testImage)
        self.photoSize = cv.GetSize(testImage)
        self.mapx = cv.CreateImage(self.photoSize, 32, 1)
        self.mapy = cv.CreateImage(self.photoSize, 32, 1)
        cv.InitUndistortMap(cv.fromarray(self.intrinsecParameters), cv.fromarray(self.distortionParameter), self.mapx, self.mapy)
        #print "CameraAccessor - initialiseUndistortMap end"

