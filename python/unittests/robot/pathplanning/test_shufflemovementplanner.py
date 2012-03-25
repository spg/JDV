import unittest
import math
from python.src.robot.pathplanning.pose import Pose
from python.src.robot.pathplanning.shufflemovementplanner import ShuffleMovementPlanner

class TestShuffleMovementPlanner(unittest.TestCase):
    def setUp(self):
        self.movementPlanner = ShuffleMovementPlanner()
        self.currentPose = Pose(0, 0, 0)

    def test_simpleMovement(self):
        path = [(1, 0)]

        moves = self.movementPlanner.planMovement(self.currentPose, path)

        self.assertEqual(1, len(moves))
        self.assertEqual(1, moves[0].distanceInCentimeters)
        self.assertEqual(0, moves[0].relativeAngleInDegrees)

    def test_simpleMovementWithAngle(self):
        path = [(1, 0), (1, 1)]

        moves = self.movementPlanner.planMovement(self.currentPose, path)

        self.assertEqual(2, len(moves))
        self.assertEqual(1, moves[0].distanceInCentimeters)
        self.assertEqual(0, moves[0].relativeAngleInDegrees)
        self.assertEqual(1, moves[1].distanceInCentimeters)
        self.assertEqual(270, moves[1].relativeAngleInDegrees)

    def test_square(self):
        path = [(1, 0), (1, 1), (0, 1), (0, 0)]

        moves = self.movementPlanner.planMovement(self.currentPose, path)

        self.assertEqual(4, len(moves))
        self.assertEqual(1, moves[0].distanceInCentimeters)
        self.assertEqual(0, moves[0].relativeAngleInDegrees)
        self.assertEqual(1, moves[1].distanceInCentimeters)
        self.assertEqual(270, moves[1].relativeAngleInDegrees)
        self.assertEqual(1, moves[2].distanceInCentimeters)
        self.assertEqual(180, moves[2].relativeAngleInDegrees)
        self.assertEqual(1, moves[3].distanceInCentimeters)
        self.assertEqual(90, moves[3].relativeAngleInDegrees)

    def test_equilateralTriangle(self):
        self.currentPose = Pose(2, 3, 180)

        path = [(5, 3), (3.5, 3 + 3 * math.cos(math.radians(30))), (2, 3)]

        moves = self.movementPlanner.planMovement(self.currentPose, path)

        delta = 0.0000001

        self.assertEqual(3, len(moves))
        self.assertEqual(3, moves[0].distanceInCentimeters)
        self.assertEqual(180, moves[0].relativeAngleInDegrees)
        self.assertEqual(3, moves[1].distanceInCentimeters)
        self.assertAlmostEqual(60, moves[1].relativeAngleInDegrees, delta=delta)
        self.assertEqual(3, moves[2].distanceInCentimeters)
        self.assertEqual(300, moves[2].relativeAngleInDegrees)