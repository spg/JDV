import unittest
from python.src.robot.pathplanning.movementplanner import MovementPlanner
from python.src.robot.pathplanning.pose import Pose

class TestMovementPlanner(unittest.TestCase):
    def setUp(self):
        self.movementPlanner = MovementPlanner()
        self.currentPose = Pose(0, 0, 0)

    def test_basicAdvanceMovement(self):
        path = [(1, 0)]

        moves = self.movementPlanner.planMovement(self.currentPose, path)

        #self.assertEqual(1, len(moves))
        #self.assertEqual(1, moves[0].distanceInCentimeters)

    def test_twoStepAdvanceMovement(self):
        path = [(1, 0), (2, 0)]

        moves = self.movementPlanner.planMovement(self.currentPose, path)

        #self.assertEqual(2, len(moves))
        #self.assertEqual(1, moves[0].distanceInCentimeters)
        #self.assertEqual(1, moves[1].distanceInCentimeters)

