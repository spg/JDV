
import cv


class Camera:
    def getDrawingContour(self):
        #ton code ici...
        # ...
        # ...
        # ton code termine, tu retournes les valeurs suivantes:

        points = [(3,5), (0,4), (100,345)] # par exemple

        zoneWidth = 600 # la largeur de la zone carrée qui contient l'image

        return points, zoneWidth


    def __init__(self):
        self.camera = cv.CaptureFromCAM(0)

    def GetFrame(self):
        return cv.QueryFrame(self.camera)