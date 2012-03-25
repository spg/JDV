from __future__ import division

import unittest
from python.src.robot.ai.math.circle import Circle
from python.src.robot.ai.math.circleexception import CircleException

class TestCircle(unittest.TestCase):
    def test_intersect_noIntersect_1(self):
        circle1 = Circle((0, 0), 1)
        circle2 = Circle((0, 3), 1)

        intersectionPoints = Circle.intersect(circle1, circle2)

        self.assertEqual(0, len(intersectionPoints))

    def test_intersect_noIntersect_2(self):
        circle1 = Circle((1, 1), 1)
        circle2 = Circle((3, 3), 1)

        intersectionPoints = Circle.intersect(circle1, circle2)

        self.assertEqual(0, len(intersectionPoints))

    def test_intersect_sameCircles(self):
        circle1 = Circle((0, 0), 1)
        circle2 = Circle((0, 0), 1)
        try:
            Circle.intersect(circle1, circle2)
            self.fail()
        except CircleException:
            pass

    def test_intersect_concentricCircles(self):
        circle1 = Circle((1, 1), 1)
        circle2 = Circle((1, 1), 2)

        intersectionPoints = Circle.intersect(circle1, circle2)

        self.assertEqual(0, len(intersectionPoints))

    def test_intersect_onePoint_1(self):
        circle1 = Circle((0, 0), 1)
        circle2 = Circle((2, 0), 1)

        intersectionPoints = Circle.intersect(circle1, circle2)

        self.assertEqual(1, len(intersectionPoints))
        self.assertEqual((1, 0), intersectionPoints[0])

    def test_intersect_onePoint_2(self):
        circle1 = Circle((4, 4), 2)
        circle2 = Circle((4, 0), 2)

        intersectionPoints = Circle.intersect(circle1, circle2)

        self.assertEqual(1, len(intersectionPoints))
        self.assertEqual((4, 2), intersectionPoints[0])

    def test_intersect_twoPoints_1(self):
        circle1 = Circle((0, 0), 2)
        circle2 = Circle((3, 0), 2)

        intersectionPoints = Circle.intersect(circle1, circle2)

        delta = 0.001

        self.assertEqual(2, len(intersectionPoints))
        self.assertAlmostEqual(1.5, intersectionPoints[0][0], delta=delta)
        self.assertAlmostEqual(-1.323, intersectionPoints[0][1], delta=delta)
        self.assertAlmostEqual(1.5, intersectionPoints[1][0], delta=delta)
        self.assertAlmostEqual(1.323, intersectionPoints[1][1], delta=delta)

    def test_intersect_twoPoints_2(self):
        circle1 = Circle((3, 2), 4)
        circle2 = Circle((6, 12), 8)

        intersectionPoints = Circle.intersect(circle1, circle2)

        delta = 0.001

        self.assertEqual(2, len(intersectionPoints))
        self.assertAlmostEqual(6.457, intersectionPoints[0][0], delta=delta)
        self.assertAlmostEqual(4.013, intersectionPoints[0][1], delta=delta)
        self.assertAlmostEqual(1.222, intersectionPoints[1][0], delta=delta)
        self.assertAlmostEqual(5.583, intersectionPoints[1][1], delta=delta)

    def test_intersect_twoPoints_3(self):
        circle1 = Circle((-3, 2), 7)
        circle2 = Circle((6, -8), 19)

        intersectionPoints = Circle.intersect(circle1, circle2)

        delta = 0.001

        self.assertEqual(2, len(intersectionPoints))
        self.assertAlmostEqual(-9.995, intersectionPoints[0][0], delta=delta)
        self.assertAlmostEqual(2.254, intersectionPoints[0][1], delta=delta)
        self.assertAlmostEqual(-2.518, intersectionPoints[1][0], delta=delta)
        self.assertAlmostEqual(8.983, intersectionPoints[1][1], delta=delta)
