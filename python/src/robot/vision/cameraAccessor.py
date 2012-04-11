import cv
import numpy

class CameraAccessor:

    def __init__(self):
        self.__initialiseCamera__()
        self.__getCalibrationParameters__()
        self.__initialiseUndistortMap__()

    def getFrame(self, undistort):
        cv.SetCaptureProperty(self.camera, cv.CV_CAP_PROP_FRAME_HEIGHT, 1200)
        cv.SetCaptureProperty(self.camera, cv.CV_CAP_PROP_FRAME_WIDTH, 1600)
        frame = cv.QueryFrame(self.camera)
        if undistort == True:
            cv.Remap(frame, frame, self.mapx, self.mapy)
        return frame

    def __getCalibrationParameters__(self):
        self.intrinsecParameters = numpy.load("vision/intrinsec.npy")
        self.distortionParameter = numpy.load("vision/distortion.npy")

    def __initialiseCamera__(self):
        print "Initialisind camera..."
        self.camera = cv.CaptureFromCAM(-1)
        cv.SetCaptureProperty(self.camera, cv.CV_CAP_PROP_FRAME_HEIGHT, 1200)
        cv.SetCaptureProperty(self.camera, cv.CV_CAP_PROP_FRAME_WIDTH, 1600)
        image = self.getFrame(False)
        print "Camera resolution : ", cv.GetSize(image)
        #cv.SetCaptureProperty(self.camera, cv.CV_CAP_PROP_FORMAT, cv.IPL_DEPTH_32F)

    def __initialiseUndistortMap__(self):
        testImage = cv.QueryFrame(self.camera) 
        #print "cameraAccessor: initialiseUndistortMap - ",  type(testImage)
        self.photoSize = cv.GetSize(testImage)
        self.mapx = cv.CreateImage(self.photoSize, cv.IPL_DEPTH_32F, 1)
        self.mapy = cv.CreateImage(self.photoSize, cv.IPL_DEPTH_32F, 1)
        cv.InitUndistortMap(cv.fromarray(self.intrinsecParameters), cv.fromarray(self.distortionParameter), self.mapx, self.mapy)

