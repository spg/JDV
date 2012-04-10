import cv
import numpy

class CameraAccessor:

    def __init__(self):
        print "CameraAccessor initialise begin"
        self.__initialiseCamera__()
        self.__getCalibrationParameters__()
        self.__initialiseUndistortMap__()
        print "CameraAccessor initialise end"

    def getFrame(self):
        print "CameraAccessor getFrame begin"
        frame = cv.QueryFrame(self.camera)
        print("#####", type(frame))
        undistortedFrame = cv.CreateImage(cv.GetSize(frame), 8, 3)
        print(">>>>>", type(undistortedFrame))

        cv.Remap(frame, undistortedFrame, self.mapx, self.mapy)
        print "CameraAccessor getFrame end"
        return undistortedFrame

    def __getCalibrationParameters__(self):
        print "CameraAccessor getCalibrationParam begin"
        self.intrinsecParameters = numpy.load("../../vision/intrinsec.npy")
        self.distortionParameter = numpy.load("../../vision/distortion.npy")
        print "CameraAccessor getCalibrationParam begin"

    def __initialiseCamera__(self):
        self.camera = cv.CaptureFromCAM(1)
        #cv.SetCaptureProperty(self.camera, cv.CV_CAP_PROP_FRAME_HEIGHT, 1200)
        #cv.SetCaptureProperty(self.camera, cv.CV_CAP_PROP_FRAME_WIDTH, 1600)
        print "CameraAccessor: initialiseCamera - set format begin"
        #cv.SetCaptureProperty(self.camera, cv.CV_CAP_PROP_FORMAT, cv.IPL_DEPTH_32F)
        print "CameraAccessor: initialiseCamera - set format end"

    def __initialiseUndistortMap__(self):
        print "CameraAccessor initialiseUndistortMap begin"
        testImage = cv.QueryFrame(self.camera) 
        #print "cameraAccessor: initialiseUndistortMap - ",  type(testImage)
        #self.photoSize = cv.GetSize(testImage)
        self.photoSize = (1600, 1200)
        self.mapx = cv.CreateImage(self.photoSize, cv.IPL_DEPTH_32F, 1)
        self.mapy = cv.CreateImage(self.photoSize, cv.IPL_DEPTH_32F, 1)
        cv.InitUndistortMap(cv.fromarray(self.intrinsecParameters), cv.fromarray(self.distortionParameter), self.mapx, self.mapy)
        print "CameraAccessor initialiseUndistortMap end"

