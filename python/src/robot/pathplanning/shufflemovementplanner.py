from python.src.robot.ai.math.vector import Vector
from python.src.robot.pathplanning.shuffle import Shuffle

class ShuffleMovementPlanner:
    def planMovement(self, currentPose, nextNodes):
        currentX = currentPose.x
        currentY = currentPose.y
        currentTheta = currentPose.theta

        currentPoseVector = Vector.buildUnitaryVectorFromAngle(currentTheta)

        moves = []

        for nextNode in nextNodes:
            destinationVector = Vector.buildFromTwoPoints((currentX, currentY), (nextNode[0], nextNode[1]))

            shuffleDistance = Vector.length(destinationVector)
            shuffleAngle = Vector.angleBetween(currentPoseVector, destinationVector)

            if shuffleAngle < 0:
                shuffleAngle += 360

            moves.append(Shuffle(shuffleDistance, shuffleAngle))

            currentX = nextNode[0]
            currentY = nextNode[1]

        return moves