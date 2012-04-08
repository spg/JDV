import unittest
from python.src.robot.util.imagepointstransformer import ImagePointsTransformer

class TestImagePointsTransformer(unittest.TestCase):
    def setUp(self):
        self.imagePointsTransformer = ImagePointsTransformer()

    def test_north_4(self):
        pointsFromImage = ([(100, 100), (350, 100), (100, 400)], 500)

        transformedPoints = self.imagePointsTransformer.transform(pointsFromImage, ImagePointsTransformer.NORTH,
            ImagePointsTransformer.SCALE_4)

        self.assertEqual([(12, 12), (42, 12), (12, 48)], transformedPoints)

    def test_east_4(self):
        pointsFromImage = ([(100, 100), (350, 100), (100, 400)], 500)

        transformedPoints = self.imagePointsTransformer.transform(pointsFromImage, ImagePointsTransformer.EAST,
            ImagePointsTransformer.SCALE_4)

        self.assertEqual([(12, 48), (12, 18), (48, 48)], transformedPoints)

    def test_west_4(self):
        pointsFromImage = ([(100, 100), (350, 100), (100, 400)], 500)

        transformedPoints = self.imagePointsTransformer.transform(pointsFromImage, ImagePointsTransformer.WEST,
            ImagePointsTransformer.SCALE_4)

        self.assertEqual([(48, 12), (48, 42), (12, 12)], transformedPoints)

    def test_west_2(self):
        pointsFromImage = ([(100, 100), (350, 100), (100, 400)], 500)

        transformedPoints = self.imagePointsTransformer.transform(pointsFromImage, ImagePointsTransformer.WEST,
            ImagePointsTransformer.SCALE_2)

        self.assertEqual([(39, 21), (39, 36), (21, 21)], transformedPoints)

    def test_west_2_square(self):
        pointsFromImage = ([(100, 400), (100, 100), (400, 100), (400,400)], 500)

        transformedPoints = self.imagePointsTransformer.transform(pointsFromImage, ImagePointsTransformer.WEST,
            ImagePointsTransformer.SCALE_2)

        self.assertEqual([(21, 21), (39, 21), (39, 39), (21, 39)], transformedPoints)