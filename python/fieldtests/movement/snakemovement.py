from python.src.robot.arduino.positioncontroller import PositionController
from python.src.robot.pathplanning.snakemovementplanner import SnakeMovementPlanner
from python.src.robot.pathplanning.pose import Pose

class RobotMover:
    def __init__(self):
        self.positionController = PositionController()

    def executeMoves(self, moves):
        for move in moves:
            if move.getType() == "Advance":
                self.positionController.advance(move.distanceInCentimeters)
            elif move.getType() == "Rotate":
                self.positionController.rotate(move.angleInDegrees)

currentPose = Pose(0, 0, 0)

path = [(10, 0), (10, 10), (20, 10), (0, 0)]

movementPlanner = SnakeMovementPlanner()
moves = movementPlanner.planMovement(currentPose, path)

robotMover = RobotMover()
robotMover.executeMoves(moves)