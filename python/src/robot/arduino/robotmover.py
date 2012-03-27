from python.src.robot.arduino.positioncontroller import PositionController
from python.src.robot.pathplanning import advance, rotate, shuffle

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