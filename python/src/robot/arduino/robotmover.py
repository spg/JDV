from python.src.robot.ai.math.vector import Vector
from python.src.robot.arduino.positioncontroller import PositionController
from python.src.robot.pathplanning import advance, rotate, shuffle
from python.src.robot.pathplanning.pathbuilder import PathBuilder
from python.src.robot.pathplanning.rotate import Rotate
from python.src.robot.pathplanning.snakemovementplanner import SnakeMovementPlanner
from python.src.robot.robot import Robot

class RobotMover:
    def __init__(self):
        self.positionController = PositionController()

    def executeMoves(self, moves):
        for move in moves:
            if move.__module__ == advance.__name__:
                self.positionController.advance(move.distanceInCentimeters)
            elif move.__module__ == rotate.__name__:
                self.positionController.rotate(move.angleInDegrees)
            elif move.__module__ == shuffle.__name__:
                self.positionController.shuffle(move.distanceInCentimeters, move.relativeAngleInDegrees)

    def doSnakeMovement(self, destination, finalAbsoluteAngle):
        pathBuilder = PathBuilder()
        path = pathBuilder.build(destination)
        del path[0]
        print path

        moves = SnakeMovementPlanner().planMovement(Robot.getCurrentPose(), path, finalAbsoluteAngle)

        print moves
        print "about to execute moves..."

        self.executeMoves(moves)