from __future__ import division

import unittest
import math
from python.src.robot.ai.math.circle import Circle
from python.src.robot.ai.math.vector import Vector

class CircleDeterminator:
    def determineCircle(self, angleBetweenP1AndP2, p1, p2):
        distanceBetweenP1andP2 = Vector.length(Vector.buildFromTwoPoints(p1, p2))
        radius = distanceBetweenP1andP2/2/math.sin(math.radians(angleBetweenP1AndP2))

        circle1 = Circle(p1, radius)
        circle2 = Circle(p2, radius)

        intersectionPoints = Circle.intersect(circle1, circle2)

        center = intersectionPoints[0]

        if len(intersectionPoints) == 2:
            v1 = Vector.buildFromTwoPoints(intersectionPoints[0], p1)
            v2 = Vector.buildFromTwoPoints(intersectionPoints[0], p2)

            angle1 = Vector.angleBetween(v1, v2)

            v1 = Vector.buildFromTwoPoints(intersectionPoints[1], p1)
            v2 = Vector.buildFromTwoPoints(intersectionPoints[1], p2)

            angle2 = Vector.angleBetween(v1, v2)

            if angle1 > angle2:
                center = intersectionPoints[0]
            else:
                center = intersectionPoints[1]

        return Circle(center, radius)

class TestCircleDeterminator(unittest.TestCase):
    def test_determineCircle_simpleCase(self):
        angle = 45
        p1 = (0, 1)
        p2 = (1, 0)

        circleDeterminator = CircleDeterminator()

        circle = circleDeterminator.determineCircle(angle, p1, p2)

        self.assertAlmostEqual(0, circle.center[0], delta=0.00001)
        self.assertAlmostEqual(0, circle.center[1], delta=0.00001)
        self.assertAlmostEqual(1, circle.radius, delta=0.00001)

    def test_determineCircle_complexCase(self):
        angle = math.degrees(math.acos(26/(5*math.sqrt(29))))
        p1 = (8, 6)
        p2 = (10, 4)

        circleDeterminator = CircleDeterminator()

        circle = circleDeterminator.determineCircle(angle, p1, p2)

        self.assertAlmostEqual(5.28571, circle.center[0], delta=0.00001)
        self.assertAlmostEqual(1.28571, circle.center[1], delta=0.00001)
        self.assertAlmostEqual(5.43984, circle.radius, delta=0.00001)

    def test_determineCircle_moreComplexCase(self):
        angle = math.degrees(1.11649)
        p1 = (-8.75, 9)
        p2 = (3, 10)

        circleDeterminator = CircleDeterminator()

        circle = circleDeterminator.determineCircle(angle, p1, p2)

        self.assertAlmostEqual(-2.63081, circle.center[0], delta=0.001)
        self.assertAlmostEqual(6.63081, circle.center[1], delta=0.001)
        self.assertAlmostEqual(6.56182, circle.radius, delta=0.001)