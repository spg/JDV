import cv
import numpy

class CameraAccessor:

    def __init__(self):
        print "CameraAccessor - initialiseCamera begin"
        self.__initialiseCamera__()
        self.__getCalibrationParameters__()
        self.__initialiseUndistortMap__()
        print "CameraAccessor - initialiseCamera end"

    def getFrame(self, undistort):
        print "CameraAccessor - getFrame begin"
        #cv.SetCaptureProperty(self.camera, cv.CV_CAP_PROP_FRAME_HEIGHT, 1200)
        #cv.SetCaptureProperty(self.camera, cv.CV_CAP_PROP_FRAME_WIDTH, 1600)
        frame = cv.QueryFrame(self.camera)
        if undistort == True:
            cv.Remap(frame, frame, self.mapx, self.mapy)
        print "CameraAccessor - getFrame end"
        return frame

    def __getCalibrationParameters__(self):
        self.intrinsecParameters = numpy.load("vision/intrinsec.npy")
        self.distortionParameter = numpy.load("vision/distortion.npy")

    def __initialiseCamera__(self):
        print "Initialising camera..."
        self.camera = cv.CaptureFromCAM(-1)
        frame = self.getFrame(False)
        print cv.GetSize(frame)
        cv.SetCaptureProperty(self.camera, cv.CV_CAP_PROP_FRAME_WIDTH, 1600)
        cv.SetCaptureProperty(self.camera, cv.CV_CAP_PROP_FRAME_HEIGHT, 1200)
        #cv.SetCaptureProperty(self.camera, cv.CV_CAP_PROP_FORMAT, cv.IPL_DEPTH_32F)

    def __initialiseUndistortMap__(self):
        print "CameraAccessor - initialiseUndistortMap begin"
        testImage = cv.QueryFrame(self.camera) 
        #print "cameraAccessor: initialiseUndistortMap - ",  type(testImage)
        self.photoSize = cv.GetSize(testImage)
        self.mapx = cv.CreateImage(self.photoSize, cv.IPL_DEPTH_32F, 1)
        self.mapy = cv.CreateImage(self.photoSize, cv.IPL_DEPTH_32F, 1)
        cv.InitUndistortMap(cv.fromarray(self.intrinsecParameters), cv.fromarray(self.distortionParameter), self.mapx, self.mapy)
        print "CameraAccessor - initialiseUndistortMap end"

