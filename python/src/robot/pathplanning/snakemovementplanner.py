from python.src.robot.ai.math.vector import Vector
from python.src.robot.pathplanning.advance import Advance
from python.src.robot.pathplanning.rotate import Rotate

class SnakeMovementPlanner():
    def planMovement(self, currentPose, nextNodes):
        currentX = currentPose.x
        currentY = currentPose.y
        currentTheta = currentPose.theta

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

        return moves