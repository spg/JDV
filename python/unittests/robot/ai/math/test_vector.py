from __future__ import division

import unittest
import math
from python.src.robot.ai.math.vector import Vector

class TestVector(unittest.TestCase):
    def test_ninetyDegrees(self):
        expectedAngle = math.radians(90)

        self.assertEqual(expectedAngle, Vector.angle([1,0],[0,1]))

    def test_minusNinetyDegrees(self):
        expectedAngle = math.radians(-90)

        self.assertEqual(expectedAngle, Vector.angle([0,1],[1,0]))

    def test_zeroDegrees(self):
        expectedAngle = math.radians(0)

        self.assertEqual(expectedAngle, Vector.angle([1,1],[2,2]))

    def test_oneEightyDegrees(self):
        expectedAngle = math.radians(180)

        self.assertEqual(expectedAngle, Vector.angle([1,0],[-1,0]))

    def test_minusOneEightyDegrees(self):
        expectedAngle = math.radians(-180)

        self.assertEqual(expectedAngle, Vector.angle([-1,0],[1,0]))

    def test_fortyFiveDegrees(self):
        expectedAngle = math.radians(45)

        self.assertEqual(expectedAngle, Vector.angle([1,0],[1,1]))

    def test_minusFortyFiveDegrees(self):
        expectedAngle = math.radians(-45)

        self.assertEqual(expectedAngle, Vector.angle([1,1],[1,0]))

    def test_thirtyDegrees(self):
        expectedAngle = math.radians(30)

        self.assertAlmostEqual(expectedAngle, Vector.angle([-math.sqrt(3)/2, -1/2],[-1/2, -math.sqrt(3)/2] ), delta=0.000000001)

    def test_minusThirtyDegrees(self):
        expectedAngle = math.radians(-30)

        self.assertAlmostEqual(expectedAngle, Vector.angle([-math.sqrt(3)/2, -1/2],[-1/2, -math.sqrt(3)/2] ), delta=0.000000001)


    