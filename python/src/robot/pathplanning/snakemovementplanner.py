from python.src.robot.ai.math.vector import Vector
from python.src.robot.pathplanning.advance import Advance
from python.src.robot.pathplanning.rotate import Rotate

class SnakeMovementPlanner():
    def planMovement(self, currentPose, nextNodes, finalAbsoluteAngle):
        currentX = currentPose[0]
        currentY = currentPose[1]
        currentTheta = currentPose[2]

        moves = []

        for nextNode in nextNodes:
            currentPoseVector = Vector.buildUnitaryVectorFromAngle(currentTheta)
            destinationVector = Vector.buildFromTwoPoints((currentX, currentY), (nextNode[0], nextNode[1]))

            rotationAngle = Vector.angleBetween(currentPoseVector, destinationVector)

            if rotationAngle:
                moves.append(Rotate(rotationAngle))

            distanceToAdvance = Vector.length(destinationVector)
            if distanceToAdvance:
                moves.append(Advance(distanceToAdvance))

            currentX = nextNode[0]
            currentY = nextNode[1]
            currentTheta += rotationAngle

        currentRobotVector = Vector.buildUnitaryVectorFromAngle(currentTheta)
        finalRobotVector = Vector.buildUnitaryVectorFromAngle(finalAbsoluteAngle)
        rotationAngle = Vector.angleBetween(currentRobotVector, finalRobotVector)

        moves.append(Rotate(rotationAngle))

        return moves