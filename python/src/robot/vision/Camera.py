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
        try:
            image = self.camera.getFrame()
            drawingImage = self.drawingExtractor.ExtractShape(image)
            contourPoints = self.contourExtractor.findContours(drawingImage)
            size = cv.GetSize(drawingImage)
            squareSize = size[0]

            for point in contourPoints:
                pointCopy = (point[0], squareSize - point[1])
                cv.Circle(drawingImage, pointCopy, 5, (0,0,0), 2)
            cv.SaveImage("segmentationResult.jpg", drawingImage)

            return contourPoints, squareSize
        except:
            raise ValueError("Couldn't find drawing in image")

    def getVisibleContours(self):
        try:
            image = self.camera.getFrame()
        except:
            raise ValueError()

    def __doubleImage__(self, contourPoints, size):
        doubleImage = cv.CreateImage((1000,1000),8,1)
        for scale in range(1,3):
            x = size[0]*scale
            y = size[1]*scale
            for i in range(len(contourPoints)):
                if i == len(contourPoints)-1:
                    x1 = contourPoints[i][0]*scale
                    y1 = contourPoints[i][1]*scale
                    x2 = contourPoints[0][0]*scale
                    y2 = contourPoints[0][1]*scale
                else:
                    x1 = contourPoints[i][0]*scale
                    y1 = contourPoints[i][1]*scale
                    x2 = contourPoints[i+1][0]*scale
                    y2 = contourPoints[i+1][1]*scale
                point1 = (x1, y1)
                point2 = (x2, y2)
                cv.Line(doubleImage,point1, point2,255, 2)

        cv.SaveImage("scale.jpg", doubleImage)