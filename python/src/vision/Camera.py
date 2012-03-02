
import cv


class Camera:

    def __init__(self):
        self.camera = cv.CaptureFromCAM(0)

    def GetFrame(self):
        return cv.QueryFrame(self.camera)