from __future__ import division

import unittest
import math
from python.src.robot.ai.math.vector import Vector

class TestVector(unittest.TestCase):
    def test_angleBetween_ninetyDegrees(self):
        self.assertEqual(90, Vector.angleBetween([1, 0], [0, 1]))

    def test_angleBetween_minusNinetyDegrees(self):
        self.assertEqual(-90, Vector.angleBetween([0, 1], [1, 0]))

    def test_angleBetween_zeroDegrees(self):
        self.assertEqual(0, Vector.angleBetween([1, 1], [2, 2]))

    def test_angleBetween_oneEightyDegrees(self):
        self.assertEqual(180, Vector.angleBetween([1, 0], [-1, 0]))

    def test_angleBetween_minusOneEightyDegrees(self):
        self.assertEqual(-180, Vector.angleBetween([-1, 0], [1, 0]))

    def test_angleBetween_fortyFiveDegrees(self):
        expectedAngle = 45

        self.assertEqual(expectedAngle, Vector.angleBetween([1, 0], [1, 1]))

    def test_angleBetween_minusFortyFiveDegrees(self):
        expectedAngle = -45

        self.assertEqual(expectedAngle, Vector.angleBetween([1, 1], [1, 0]))

    def test_angleBetween_thirtyDegrees(self):
        expectedAngle = 30

        self.assertAlmostEqual(expectedAngle,
            Vector.angleBetween([-math.sqrt(3) / 2, -1 / 2], [-1 / 2, -math.sqrt(3) / 2]),
            delta=0.000000001)

    def test_angleBetween_minusThirtyDegrees(self):
        self.assertAlmostEqual(-30,
            Vector.angleBetween([-1 / 2, -math.sqrt(3) / 2], [-math.sqrt(3) / 2, -1 / 2]),
            delta=0.000000001)

    def test_angleBetween_largeRotation(self):
        expectedAngle = math.degrees(math.acos(2/math.sqrt(1229)))

        self.assertAlmostEqual(expectedAngle,
            Vector.angleBetween([-1, 0], [-2, -35]),
            delta=0.000000001)

    def test_angleBetween_ninetyDegreesLargeRotation(self):
        self.assertAlmostEqual(90,
            Vector.angleBetween([-1, 0], [0, -1]),
            delta=0.000000001)

    def test_angleBetween_minusNinetyDegreesLargeRotation(self):
        self.assertAlmostEqual(-90,
            Vector.angleBetween([0, -1],[-1, 0]),
            delta=0.000000001)

    def test_buildFromTwoPoints_simpleCase(self):
        p1 = (0, 0)
        p2 = (1, 0)

        vector = Vector.buildFromTwoPoints(p1, p2)

        self.assertEqual([1, 0], vector)

    def test_buildFromTwoPoints_simpleCase_2(self):
        p1 = (8, 6)
        p2 = (9, 6)

        vector = Vector.buildFromTwoPoints(p1, p2)

        self.assertEqual([1, 0], vector)

    def test_buildFromTwoPoints_simpleCase_3(self):
        p1 = (9, 6)
        p2 = (8, 6)

        vector = Vector.buildFromTwoPoints(p1, p2)

        self.assertEqual([-1, 0], vector)

    def test_buildFromTwoPoints_simpleCase_4(self):
        p1 = (8, 6)
        p2 = (8, 6)

        vector = Vector.buildFromTwoPoints(p1, p2)

        self.assertEqual([0, 0], vector)

    def test_buildFromTwoPoints_simpleCase_5(self):
        p1 = (8, 5)
        p2 = (8, 6)

        vector = Vector.buildFromTwoPoints(p1, p2)

        self.assertEqual([0, 1], vector)

    def test_buildFromTwoPoints_simpleCase_6(self):
        p1 = (8, 6)
        p2 = (8, 5)

        vector = Vector.buildFromTwoPoints(p1, p2)

        self.assertEqual([0, -1], vector)

    def test_buildFromTwoPoints_complexCase_1(self):
        p1 = (-1, -1)
        p2 = (1, 1)

        vector = Vector.buildFromTwoPoints(p1, p2)

        self.assertEqual([2, 2], vector)

    def test_buildFromTwoPoints_complexCase_2(self):
        p1 = (-6, 8)
        p2 = (3, 2)

        vector = Vector.buildFromTwoPoints(p1, p2)

        self.assertEqual([9, -6], vector)

    def test_buildFromTwoPoints_complexCase_3(self):
        p1 = (26.3, -11.5)
        p2 = (23.1, 2)

        vector = Vector.buildFromTwoPoints(p1, p2)

        self.assertAlmostEqual(-3.2, vector[0], delta=0.0000001)
        self.assertEqual(13.5, vector[1])

    def test_length_zero(self):
        self.assertEqual(0, Vector.length([0, 0]))

    def test_length_one(self):
        self.assertEqual(1, Vector.length([0, 1]))

    def test_length_sqrt2(self):
        self.assertEqual(math.sqrt(2), Vector.length([1, 1]))

    def test_length_negativeValues(self):
        self.assertEqual(math.sqrt(20), Vector.length([-2, -4]))

    def test_buildUnitaryVectorFromAngle_zero(self):
        vector = Vector.buildUnitaryVectorFromAngle(0)

        self.assertEqual([1, 0], vector)

    def test_buildUnitaryVectorFromAngle_ninety(self):
        vector = Vector.buildUnitaryVectorFromAngle(90)

        self.assertAlmostEqual(0, vector[0], delta=0.000001)
        self.assertEqual(1, vector[1])

    def test_buildUnitaryVectorFromAngle_210(self):
        vector = Vector.buildUnitaryVectorFromAngle(210)

        self.assertAlmostEqual(-math.sqrt(3)/2, vector[0], delta=0.000001)
        self.assertAlmostEqual(-0.5, vector[1], delta=0.0000001)