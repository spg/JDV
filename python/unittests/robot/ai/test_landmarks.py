import unittest
from python.src.robot.ai.landmarks import Landmarks

class TestLandmarks(unittest.TestCase):
    def test_artag1(self):
        self.assertEqual((0,1), Landmarks.ARTAG1.position)