from python.src.robot.arduino.positioncontroller import PositionController
from python.src.robot.pathplanning.advance import Advance
from python.src.robot.pathplanning.snakemovementplanner import SnakeMovementPlanner
from python.src.robot.pathplanning.pose import Pose
from python.src.robot.pathplanning.rotate import Rotate

class RobotMover:
    def __init__(self):
        self.positionController = PositionController()

    def executeMoves(self, moves):
        for move in moves:
            if type(move) is Advance:
                self.positionController.advance(move.distanceInCentimeters)
            elif type(move) is Rotate:
                self.positionController.rotate(move.angleInDegrees)

currentPose = Pose(0, 0, 0)

path = [(7, -8), (-8, 7), (-5, -3), (0, 0)]

movementPlanner = SnakeMovementPlanner()
moves = movementPlanner.planMovement(currentPose, path)

robotMover = RobotMover()
robotMover.executeMoves(moves)

positionctrl = PositionController()
positionctrl.advance(10)