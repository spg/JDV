from __future__ import division

import unittest
import math
from python.src.robot.ai.math.circle import Circle
from python.src.robot.ai.math.vector import Vector

class CircleDeterminator:
    def determineCircle(self, angleBetweenP1AndP2, p1, p2):
        distanceBetweenP1andP2 = Vector.length(Vector.buildFromTwoPoints(p1, p2))
        r = distanceBetweenP1andP2/2/math.cos(math.radians(angleBetweenP1AndP2))

        c1 = Circle(p1, r)
        c2 = Circle(p2, r)

        intersect = Circle.intersect(c1, c2)
        print intersect

class TestCircleDeterminator(unittest.TestCase):
    def test_determineCircle_simpleCase(self):
        angle = 45
        p1 = (1.0, 0)
        p2 = (0, 1)

        circleDeterminator = CircleDeterminator()
        circleDeterminator.determineCircle(angle, p1, p2)
