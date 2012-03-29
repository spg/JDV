import unittest
from python.src.robot.ai.math.circle import Circle
from python.unittests.robot.ai.positionacquisition.test_angleextractor import AngleExtractor
from python.unittests.robot.ai.positionacquisition.test_circledeterminator import CircleDeterminator

class PositionProvider:
    def __init__(self):
        self.angleExtractor = AngleExtractor()
        self.circleDeterminator = CircleDeterminator()


    def providePosition(self, focalDistance, p1, d1, p2, d2, p3, d3):
        a1, a2 = self.angleExtractor.extractAngle(focalDistance, p1, d1, p2, d2, p3, d3)

        circle1 = self.circleDeterminator.determineCircle(a1, p1, p2)
        circle2 = self.circleDeterminator.determineCircle(a2, p2, p3)

        intersections = Circle.intersect(circle1, circle2)

        return intersections


class TestPositionProvider(unittest.TestCase):
    def test_simpleCase(self):
        p1 = (0,0)
        p2 = (2,3)
        p3 = (8,2)

        intersections = PositionProvider().providePosition(100, p1, 20, p2, 35, p3, 58)

        self.assertAlmostEqual(8, 8)

    def test_simpleCase_2(self):
        p1 = (-2,-2)
        p2 = (0,0)
        p3 = (2,-2)

        intersections = PositionProvider().providePosition(20, p1, -2, p2, 0, p3, 2)

        self.assertAlmostEqual(8, 8)