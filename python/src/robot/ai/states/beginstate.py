import time
from python.src.robot.ai.statecontroller import StateController
from python.src.robot.ai.states.state import State
from python.src.robot.arduino.robotmover import RobotMover
from python.src.robot.pathplanning.pose import Pose
from python.src.robot.robot import Robot
from python.src.robot.terrain import Terrain

class BeginState(State):
    def __init__(self, obstacle1, obstacle2):
        Terrain.OBSTACLE_1 = obstacle1
        Terrain.OBSTACLE_2 = obstacle2

    def run(self):
        robotMover = RobotMover()

        robotMover.doSnakeMovement(Terrain.FIGURE_5_FACE, 180)

        Robot.currentPose = Pose(Terrain.FIGURE_5_FACE[0], Terrain.FIGURE_5_FACE[1], 180)

        time.sleep(3)

        robotMover.doSnakeMovement(Terrain.DRAWING_ZONE_CENTER, 270)

        Robot.currentPose = Pose(Terrain.DRAWING_ZONE_CENTER[0], Terrain.FIGURE_5_FACE[1], 180)

        StateController.instance.endMainLoop()