import cv
import math
class ShapeExtractor:

    def ExtractShape(self, srcImage):

        shapeImage = cv.CreateImage(cv.GetSize(srcImage), 8, 1)
        tmpImage = cv.CreateImage(cv.GetSize(srcImage), 8, 1)
        tmpImage2 = cv.CreateImage(cv.GetSize(srcImage), 8, 1)

        points = cv.GoodFeaturesToTrack(srcImage,tmpImage,tmpImage2, 100, 0.01, 10, None, 3, 0, 0.04)

        for point in points:
            x = int(point[0])
            y = int(point[1])

            center = int(point[0]), int(point[1])
            cv.Circle(srcImage, (center), 4, (0,0,255))

        return shapeImage