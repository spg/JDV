import math
from python.src.robot.arduino.positioncontroller import PositionController
from python.src.robot.pathplanning import advance, rotate, shuffle
from python.src.robot.pathplanning.pathbuilder import PathBuilder
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
                self.__sendPoseToBase_advance(move.distanceInCentimeters)
            elif move.__module__ == rotate.__name__:
                self.positionController.rotate(move.angleInDegrees)
                self.__sendPoseToBase_rotate(move.angleInDegrees)
            elif move.__module__ == shuffle.__name__:
                self.positionController.shuffle(move.distanceInCentimeters, move.relativeAngleInDegrees)
                self.__sendPoseToBase_shuffle(move.distanceInCentimeters)

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

    def __sendPoseToBase_advance(self, distanceInCentimeters):
        currentPose = Robot.getCurrentPose()

        deltaY = math.sin(math.radians(currentPose[2])) * distanceInCentimeters
        deltaX = math.cos(math.radians(currentPose[2])) * distanceInCentimeters

        Robot.setCurrentPose((currentPose[0] + deltaX, currentPose[1] - deltaY, currentPose[2]))

    def __sendPoseToBase_rotate(self, angleInDegrees):
        currentPose = Robot.getCurrentPose()

        Robot.setCurrentPose((currentPose[0], currentPose[1], currentPose[2] + angleInDegrees))

    def __sendPoseToBase_shuffle(self, distanceInCentimeters):
        currentPose = Robot.getCurrentPose()

        deltaY = math.sin(math.radians(currentPose[2])) * distanceInCentimeters
        deltaX = math.cos(math.radians(currentPose[2])) * distanceInCentimeters

        Robot.setCurrentPose((currentPose[0] + deltaX, currentPose[1] - deltaY, currentPose[2]))