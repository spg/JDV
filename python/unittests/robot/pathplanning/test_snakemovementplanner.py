from __future__ import division

import unittest
import math
from python.src.robot.pathplanning.snakemovementplanner import SnakeMovementPlanner
from python.src.robot.pathplanning.pose import Pose
from python.src.robot.terrain import Terrain

class TestSnakeMovementPlanner(unittest.TestCase):
    def setUp(self):
        self.movementPlanner = SnakeMovementPlanner()
        self.currentPose = (0, 0, 0)

    def test_planMovement_basicAdvanceMovement(self):
        path = [(1, 0)]

        moves = self.movementPlanner.planMovement(self.currentPose, path, 0)

        self.assertEqual(1, len(moves))
        self.assertEqual(1, moves[0].distanceInCentimeters)

    def test_planMovement_twoStepAdvanceMovement(self):
        path = [(1, 0), (2, 0)]

        moves = self.movementPlanner.planMovement(self.currentPose, path, 0)

        self.assertEqual(2, len(moves))
        self.assertEqual(1, moves[0].distanceInCentimeters)
        self.assertEqual(1, moves[1].distanceInCentimeters)

    def test_planMovement_simpleAngle(self):
        path = [(0, 1)]

        moves = self.movementPlanner.planMovement(self.currentPose, path, 270)

        self.assertEqual(2, len(moves))
        self.assertEqual(-90, moves[0].angleInDegrees)
        self.assertEqual(1, moves[1].distanceInCentimeters)

    def test_planMovement_twoSimpleAngles(self):
        path = [(0, 1), (1, 1)]

        moves = self.movementPlanner.planMovement(self.currentPose, path, 0)

        self.assertEqual(4, len(moves))
        self.assertEqual(-90, moves[0].angleInDegrees)
        self.assertEqual(1, moves[1].distanceInCentimeters)
        self.assertEqual(90, moves[2].angleInDegrees)
        self.assertEqual(1, moves[3].distanceInCentimeters)

    def test_planMovement_complexMovement_1(self):
        self.currentPose = (9, 27, 180)

        path = [(7, -8), (-8, 7), (-5, -3), (0, 0)]

        moves = self.movementPlanner.planMovement(self.currentPose, path, 360 - math.degrees(math.atan(3/5)))

        delta = 0.0000001

        self.assertEqual(8, len(moves))
        self.assertAlmostEqual(-1*math.degrees(math.acos(2/math.sqrt(1229))), moves[0].angleInDegrees, delta=delta)
        self.assertAlmostEqual(math.sqrt(1229), moves[1].distanceInCentimeters, delta=delta)
        self.assertAlmostEqual(math.degrees(math.acos(-33/math.sqrt(2458))), moves[2].angleInDegrees, delta=delta)
        self.assertAlmostEqual(math.sqrt(450), moves[3].distanceInCentimeters, delta=delta)
        self.assertAlmostEqual(-1*math.degrees(math.acos(-13/math.sqrt(218))), moves[4].angleInDegrees, delta=delta)
        self.assertAlmostEqual(math.sqrt(109), moves[5].distanceInCentimeters, delta=delta)
        self.assertAlmostEqual(-1*math.degrees(math.acos(-15/math.sqrt(3706))), moves[6].angleInDegrees, delta=delta)
        self.assertAlmostEqual(math.sqrt(34), moves[7].distanceInCentimeters, delta=delta)

    def test_planMovement_fieldTest_1(self):
        path = [(10, 0), (10, 10), (20, 10), (0, 0)]

        moves = self.movementPlanner.planMovement(self.currentPose, path, 153.434949)

        delta = 0.0000001

        self.assertEqual(7, len(moves))
        self.assertAlmostEqual(10, moves[0].distanceInCentimeters, delta=delta)
        self.assertAlmostEqual(-90, moves[1].angleInDegrees, delta=delta)
        self.assertAlmostEqual(10, moves[2].distanceInCentimeters, delta=delta)
        self.assertAlmostEqual(90, moves[3].angleInDegrees, delta=delta)
        self.assertAlmostEqual(10, moves[4].distanceInCentimeters, delta=delta)


    def test_planMovement_hello(self):
        self.currentPose = (Terrain.FIGURE_6_FACE[0], Terrain.FIGURE_6_FACE[1], 180)

        path = [(10, 0), (10, 10), (20, 10), (0, 0)]

        moves = self.movementPlanner.planMovement(self.currentPose, path, 153.434949)

    def test_planMovement_fieldTest_2(self):
        self.currentPose = (180.1, Terrain.DRAWING_ZONE_NORTH_EAST_CORNER_OUTER[1], 180)

        path = [(Terrain.DRAWING_ZONE_SOUTH_EAST_CORNER_OUTER[0], Terrain.DRAWING_ZONE_SOUTH_EAST_CORNER_OUTER[1])]

        moves = self.movementPlanner.planMovement(self.currentPose, path, 0)

        delta = 0.0000001

        self.assertEqual(7, len(moves))
        self.assertAlmostEqual(10, moves[0].distanceInCentimeters, delta=delta)
        self.assertAlmostEqual(-90, moves[1].angleInDegrees, delta=delta)
        self.assertAlmostEqual(10, moves[2].distanceInCentimeters, delta=delta)
        self.assertAlmostEqual(90, moves[3].angleInDegrees, delta=delta)
        self.assertAlmostEqual(10, moves[4].distanceInCentimeters, delta=delta)