from __future__ import division

import unittest
from python.src.robot.util.pointscloudscaler import PointsCloudOperations

class TestPointsCloudScaler(unittest.TestCase):
    def test_scale_simpleCase_1(self):
        cloud = [(0, 0), (2, 0), (2, 2), (0, 2)]

        self.assertEqual([(0, 0), (1, 0), (1, 1), (0, 1)], PointsCloudOperations.scale(cloud, 0.5))

    def test_scale_simpleCase_2(self):
        cloud = [(1, 1), (2, 2), (2, 0), (0, 0)]

        self.assertEqual([(2, 2), (4, 4), (4, 0), (0, 0)], PointsCloudOperations.scale(cloud, 2))

    def test_scale_simpleCase_3(self):
        cloud = [(100, 100), (250, 80), (400, 400), (0, 0)]

        self.assertEqual([(15, 15), (37.5, 12), (60, 60), (0, 0)], PointsCloudOperations.scale(cloud, 60 / 400))

    def test_scale_simpleCase_4(self):
        cloud = [(103, 90), (254, 78), (691, 690), (3, 4)]

        self.assertEqual([(8.24, 7.2), (20.32, 6.24), (55.28, 55.2), (0.24, 0.32)],
            PointsCloudOperations.scale(cloud, 60 / 750))

    def test_move_simpleCase_1(self):
        cloud = [(0, 0), (2, 0), (2, 2), (0, 2)]

        self.assertEqual([(1, 1), (3, 1), (3, 3), (1, 3)], PointsCloudOperations.move(cloud, 1, 1))

    def test_move_simpleCase_2(self):
        cloud = [(1, 1), (2, 2), (2, 0), (0, 0)]

        self.assertEqual([(1, 1), (2, 2), (2, 0), (0, 0)], PointsCloudOperations.move(cloud, 0, 0))

    def test_move_simpleCase_3(self):
        cloud = [(100, 100), (250, 80), (400, 400), (0, 0)]

        self.assertEqual([(90, 110), (240, 90), (390, 410), (-10, 10)], PointsCloudOperations.move(cloud, -10, 10))

    def test_move_simpleCase_4(self):
        cloud = [(103, 90), (254, 78), (691, 690), (3, 4)]

        self.assertEqual([(92.5, 93), (243.5, 81), (680.5, 693), (-7.5, 7)],
            PointsCloudOperations.move(cloud, -10.5, 3))