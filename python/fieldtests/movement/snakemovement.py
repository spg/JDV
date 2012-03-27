from python.src.robot.arduino.robotmover import RobotMover
from python.src.robot.pathplanning.snakemovementplanner import SnakeMovementPlanner
from python.src.robot.pathplanning.pose import Pose

currentPose = Pose(0, 0, 0)

path = [(10, 0), (10, 10), (20, 10), (0, 0)]

movementPlanner = SnakeMovementPlanner()
moves = movementPlanner.planMovement(currentPose, path)

robotMover = RobotMover()
robotMover.executeMoves(moves)