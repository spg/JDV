import math

class Vector:
    @staticmethod
    def angle(v1, v2):
        return math.atan2(v2[1],v2[0]) - math.atan2(v1[1],v1[0])

    @staticmethod
    def buildFromTwoPoints(p1, p2):
        x1 = p1[0]
        x2 = p2[0]

        y1 = p1[1]
        y2 = p2[1]

        deltaX = x2 - x1
        deltaY = y2 - y1

        return [deltaX, deltaY]