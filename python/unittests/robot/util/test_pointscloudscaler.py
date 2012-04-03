from __future__ import division

import unittest
from python.src.robot.util.pointscloudscaler import PointsCloudScaler

class TestPointsCloudScaler(unittest.TestCase):
    def test_scalePointsCloud_simpleCase_1(self):
        cloud = [(0,0), (2,0), (2,2), (0,2)]

        self.assertEqual([(0,0), (1,0), (1,1), (0,1)], PointsCloudScaler.scalePointsCloud(cloud, 0.5))

    def test_scalePointsCloud_simpleCase_2(self):
        cloud = [(1,1), (2,2), (2,0), (0,0)]

        self.assertEqual([(2,2), (4,4), (4,0), (0,0)], PointsCloudScaler.scalePointsCloud(cloud, 2))

    def test_scalePointsCloud_simpleCase_3(self):
        cloud = [(100, 100), (250,80), (400,400), (0,0)]

        self.assertEqual([(15,15), (37.5, 12), (60,60), (0,0)], PointsCloudScaler.scalePointsCloud(cloud, 60/400))

    def test_scalePointsCloud_simpleCase_4(self):
        cloud = [(103, 90), (254,78), (691,690), (3,4)]

        self.assertEqual([(8.24, 7.2), (20.32, 6.24), (55.28, 55.2), (0.24, 0.32)], PointsCloudScaler.scalePointsCloud(cloud, 60/750))