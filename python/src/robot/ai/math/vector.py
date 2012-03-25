import math

class Vector:
    @staticmethod
    def length(vector):
        return math.sqrt(math.pow(vector[0], 2) + math.pow(vector[1], 2))

    @staticmethod
    def angleBetween(v1, v2):
        angle = math.degrees(math.atan2(v1[1],v1[0])- math.atan2(v2[1],v2[0]))

        if math.fabs(angle) > 180:
            if angle < 0:
                angle += 360
            else:
                angle -= 360

        return angle

    @staticmethod
    def buildFromTwoPoints(p1, p2):
        x1 = p1[0]
        x2 = p2[0]

        y1 = p1[1]
        y2 = p2[1]

        deltaX = x2 - x1
        deltaY = y2 - y1

        return [deltaX, deltaY]

    #builds a vector of magnitude 1, from an angle in degrees
    @staticmethod
    def buildUnitaryVectorFromAngle(angleInDegrees):
        angleInRadians = math.radians(-1*angleInDegrees)

        x = math.cos(angleInRadians)
        y = math.sin(angleInRadians)

        return [x, y]