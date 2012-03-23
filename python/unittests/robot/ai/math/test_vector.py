from __future__ import division

import unittest
import math
from python.src.robot.ai.math.vector import Vector

class TestVector(unittest.TestCase):
    def test_ninetyDegrees(self):
        expectedAngle = math.radians(90)

        self.assertEqual(expectedAngle, Vector.angle([1, 0], [0, 1]))

    def test_minusNinetyDegrees(self):
        expectedAngle = math.radians(-90)

        self.assertEqual(expectedAngle, Vector.angle([0, 1], [1, 0]))

    def test_zeroDegrees(self):
        expectedAngle = math.radians(0)

        self.assertEqual(expectedAngle, Vector.angle([1, 1], [2, 2]))

    def test_oneEightyDegrees(self):
        expectedAngle = math.radians(180)

        self.assertEqual(expectedAngle, Vector.angle([1, 0], [-1, 0]))

    def test_minusOneEightyDegrees(self):
        expectedAngle = math.radians(-180)

        self.assertEqual(expectedAngle, Vector.angle([-1, 0], [1, 0]))

    def test_fortyFiveDegrees(self):
        expectedAngle = math.radians(45)

        self.assertEqual(expectedAngle, Vector.angle([1, 0], [1, 1]))

    def test_minusFortyFiveDegrees(self):
        expectedAngle = math.radians(-45)

        self.assertEqual(expectedAngle, Vector.angle([1, 1], [1, 0]))

    def test_thirtyDegrees(self):
        expectedAngle = math.radians(30)

        self.assertAlmostEqual(expectedAngle, Vector.angle([-math.sqrt(3) / 2, -1 / 2], [-1 / 2, -math.sqrt(3) / 2]),
            delta=0.000000001)

    def test_minusThirtyDegrees(self):
        expectedAngle = math.radians(-30)

        self.assertAlmostEqual(expectedAngle, Vector.angle([-1 / 2, -math.sqrt(3) / 2], [-math.sqrt(3) / 2, -1 / 2]),
            delta=0.000000001)


    def test_buildFromTwoPoints_simpleCase(self):
        p1 = (0, 0)
        p2 = (1, 0)

        vector = Vector.buildFromTwoPoints(p1, p2)

        self.assertEqual(1, vector[0])
        self.assertEqual(0, vector[1])

    def test_buildFromTwoPoints_simpleCase_2(self):
        p1 = (8, 6)
        p2 = (9, 6)

        vector = Vector.buildFromTwoPoints(p1, p2)

        self.assertEqual(1, vector[0])
        self.assertEqual(0, vector[1])

    def test_buildFromTwoPoints_simpleCase_3(self):
        p1 = (9, 6)
        p2 = (8, 6)

        vector = Vector.buildFromTwoPoints(p1, p2)

        self.assertEqual(-1, vector[0])
        self.assertEqual(0, vector[1])

    def test_buildFromTwoPoints_simpleCase_4(self):
        p1 = (8, 6)
        p2 = (8, 6)

        vector = Vector.buildFromTwoPoints(p1, p2)

        self.assertEqual(0, vector[0])
        self.assertEqual(0, vector[1])

    def test_buildFromTwoPoints_simpleCase_5(self):
        p1 = (8, 5)
        p2 = (8, 6)

        vector = Vector.buildFromTwoPoints(p1, p2)

        self.assertEqual(0, vector[0])
        self.assertEqual(1, vector[1])

    def test_buildFromTwoPoints_simpleCase_6(self):
        p1 = (8, 6)
        p2 = (8, 5)

        vector = Vector.buildFromTwoPoints(p1, p2)

        self.assertEqual(0, vector[0])
        self.assertEqual(-1, vector[1])

    def test_buildFromTwoPoints_complexCase_1(self):
        p1 = (-1, -1)
        p2 = (1, 1)

        vector = Vector.buildFromTwoPoints(p1, p2)

        self.assertEqual(2, vector[0])
        self.assertEqual(2, vector[1])

    def test_buildFromTwoPoints_complexCase_2(self):
        p1 = (-6, 8)
        p2 = (3, 2)

        vector = Vector.buildFromTwoPoints(p1, p2)

        self.assertEqual(9, vector[0])
        self.assertEqual(-6, vector[1])

    def test_buildFromTwoPoints_complexCase_3(self):
        p1 = (26.3, -11.5)
        p2 = (23.1, 2)

        vector = Vector.buildFromTwoPoints(p1, p2)

        self.assertAlmostEqual(-3.2, vector[0], delta=0.0000001)
        self.assertEqual(13.5, vector[1])