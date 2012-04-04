from python.src.robot.ai.math.vector import Vector
from python.src.robot.arduino.positioncontroller import PositionController
from python.src.robot.pathplanning import advance, rotate, shuffle
from python.src.robot.pathplanning.pathbuilder import PathBuilder
from python.src.robot.pathplanning.rotate import Rotate
from python.src.robot.pathplanning.shufflemovementplanner import ShuffleMovementPlanner
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

    def __buildPath(self, destination):
        pathBuilder = PathBuilder()
        path = pathBuilder.build(destination)
        del path[0]
        print path

        return path

    def doSnakeMovement(self, destination, finalAbsoluteAngle):
        path = self.__buildPath(destination)

        moves = SnakeMovementPlanner().planMovement(Robot.getCurrentPose(), path, finalAbsoluteAngle)

        print "about to execute snake moves..."
        print moves

        self.executeMoves(moves)

        Robot.setCurrentPose((destination[0], destination[1], finalAbsoluteAngle))

    def doShuffleMovement(self, path):
        print "about to delete first node on shuffle path..."
        print "node to delete is: " + str(path[0])
        del path[0] # path[0] is the current robot's pose

        print "planning shuffle movement..."
        moves = ShuffleMovementPlanner().planMovement(Robot.getCurrentPose(), path)

        print "about to execute shuffle moves..."
        print moves

        self.executeMoves(moves)

        lastNode = path[len(path) - 1]
        Robot.setCurrentPose((lastNode[0], lastNode[1], 270))