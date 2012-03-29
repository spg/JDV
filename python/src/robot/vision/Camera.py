from cameraAccessor import CameraAccessor
from DrawingExtractor import DrawingExtractor
from ContourExtractor import ContourExtractor
import cv2.cv as cv

class Camera:
    def __init__(self):
        self.camera = CameraAccessor()
        self.drawingExtractor = DrawingExtractor()
        self.contourExtractor = ContourExtractor()

    def getDrawingContour(self):
        image = self.camera.getFrame()
        drawingImage = self.drawingExtractor.ExtractShape(image)
        contourPoints = self.contourExtractor.findContours(drawingImage)
        size = cv.GetSize(drawingImage)
        squareSize = size[0]

        for point in contourPoints:
            cv.Circle(drawingImage, point, 5, (0,0,0), 2)
        cv.SaveImage("segmentationResult.jpg", drawingImage)

        return contourPoints, squareSize