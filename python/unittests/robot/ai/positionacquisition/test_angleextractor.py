from __future__ import division

import unittest
import math

class AngleExtractor:
    def extractAngle(self, focalDistance, p1, d1, p2, d2, p3, d3):
        self.focalDistance = focalDistance

        self.p1 = p1
        self.d1 = d1
        self.p2 = p2
        self.d2 = d2
        self.p3 = p3
        self.d3 = d3

        self.a1 = 1
        self.a2 = 1

        if 0 < d1 < d2 < d3:
            self.__treatCaseOne()
        elif d1 < 0 < d2 < d3:
            self.__treatCaseTwo()
        elif d1 < d2 < 0 < d3:
            self.__treatCaseThree()
        else:
            self.__treatCaseFour()

        return self.a1, self.a2

    def __treatCaseOne(self):
        self.a1 = self.__atan(self.d2) - self.__atan(self.d1)
        self.a2 = self.__atan(self.d3) - self.__atan(self.d2)

    def __treatCaseTwo(self):
        self.a1 = self.__atan(-self.d1) + self.__atan(self.d2)
        self.a2 = self.__atan(self.d3) - self.__atan(self.d2)

    def __treatCaseThree(self):
        self.a1 = self.__atan(-self.d1) - self.__atan(-self.d2)
        self.a2 = self.__atan(-self.d2) + self.__atan(self.d3)

    def __treatCaseFour(self):
        self.a1 = self.__atan(-self.d1) - self.__atan(-self.d2)
        self.a2 = self.__atan(-self.d2) - self.__atan(-self.d3)

    def __atan(self, d):
        return math.degrees(math.atan(d / self.focalDistance))


class TestAngleExtractor(unittest.TestCase):
    def setUp(self):
        self.angleExtractor = AngleExtractor()

    def test_extractAngles_allPositiveDistances(self):
        focalDistance = 20

        a1, a2 = self.angleExtractor.extractAngle(focalDistance, "p1", 10, "p2", 40, "p3", 60)

        self.assertAlmostEqual(36.8698, a1, delta=0.0001)
        self.assertAlmostEqual(8.1301, a2, delta=0.0001)

    def test_extractAngles_d1_IsNegative(self):
        focalDistance = 100

        a1, a2 = self.angleExtractor.extractAngle(focalDistance, "p1", -40.8, "p2", 20, "p3", 110)

        self.assertAlmostEqual(33.50533, a1, delta=0.0001)
        self.assertAlmostEqual(36.4163, a2, delta=0.0001)

    def test_extractAngles_d1_And_d2_AreNegative(self):
        focalDistance = 70

        a1, a2 = self.angleExtractor.extractAngle(focalDistance, "p1", -120.3, "p2", -45, "p3", 34)

        self.assertAlmostEqual(27.0706, a1, delta=0.0001)
        self.assertAlmostEqual(58.6417, a2, delta=0.0001)

    def test_extractAngles_allDistancesAreNegative(self):
        focalDistance = 235.8

        a1, a2 = self.angleExtractor.extractAngle(focalDistance, "p1", -210.9, "p2", -98, "p3", -5)

        self.assertAlmostEqual(19.2414, a1, delta=0.0001)
        self.assertAlmostEqual(21.3534, a2, delta=0.0001)