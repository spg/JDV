import unittest
from python.src.robot.util.pointscloudscaler import PointsCloudScaler

class TestPointsCloudScaler(unittest.TestCase):
    def test_scalePointsCloud_simpleCase_1(self):
        cloud = [(0,0), (2,0), (2,2), (0,2)]

        self.assertEqual([(0,0), (1,0), (1,1), (0,1)], PointsCloudScaler.scalePointsCloud(cloud, 0.5))

    def test_scalePointsCloud_simpleCase_2(self):
        cloud = [(1,1), (2,2), (2,0), (0,0)]

        self.assertEqual([(2,2), (4,4), (4,0), (0,0)], PointsCloudScaler.scalePointsCloud(cloud, 2))