import math
from python.src.robot.ai.math.circleexception import CircleException
from python.src.robot.ai.math.vector import Vector

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    # see here for algorithm: http://local.wasp.uwa.edu.au/~pbourke/geometry/2circle/
    @staticmethod
    def intersect(circle1, circle2):
        x1 = circle1.center[0]
        y1 = circle1.center[1]
        r1 = circle1.radius

        x2 = circle2.center[0]
        y2 = circle2.center[1]
        r2 = circle2.radius

        distanceBetweenCenters = Vector.length((x2 - x1, y2 - y1))

        if distanceBetweenCenters > r1 + r2 or distanceBetweenCenters < math.fabs(r1 - r2):
            return []
        elif distanceBetweenCenters == 0 and r1 == r2:
            raise CircleException("The two circles are the same")

        a = (math.pow(r1, 2) - math.pow(r2, 2) + math.pow(distanceBetweenCenters, 2)) / (2 * distanceBetweenCenters)

        p2x = x1 + a * (x2 - x1) / distanceBetweenCenters
        p2y = y1 + a * (y2 - y1) / distanceBetweenCenters

        if a == r1:
            return [(p2x, p2y)]

        h = math.sqrt(math.pow(r1, 2) - math.pow(a, 2))

        p3x = p2x + h*(y2 - y1)/distanceBetweenCenters
        p3y = p2y - h*(x2 - x1)/distanceBetweenCenters

        p4x = p2x - h*(y2 - y1)/distanceBetweenCenters
        p4y = p2y + h*(x2 - x1)/distanceBetweenCenters

        return [(p3x, p3y), (p4x, p4y)]