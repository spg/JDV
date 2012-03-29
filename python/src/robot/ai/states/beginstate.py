import time
from python.src.robot.ai.statecontroller import StateController
from python.src.robot.ai.states.state import State
from python.src.robot.arduino.robotmover import RobotMover
from python.src.robot.robot import Robot
from python.src.robot.terrain import Terrain

class BeginState(State):
    def __init__(self, obstacle1, obstacle2):
        Terrain.OBSTACLE_1 = obstacle1
        Terrain.OBSTACLE_2 = obstacle2

    def run(self):
        Robot.setCurrentPose((207.8, 22.5, 90))

        print "running..."
        robotMover = RobotMover()

        print "doing snake movement 1..."
        robotMover.doSnakeMovement(Terrain.FIGURE_6_FACE, 270)
        print "snake movement 1 over!"

        Robot.setCurrentPose((Terrain.FIGURE_6_FACE[0], Terrain.FIGURE_6_FACE[1], 270))

        time.sleep(3)

        print "doing snake movement 2..."
        robotMover.doSnakeMovement(Terrain.DRAWING_ZONE_CENTER, 270)
        print "snake movement 2 over!"

        #Robot.setCurrentPose((Terrain.DRAWING_ZONE_CENTER[0], Terrain.FIGURE_5_FACE[1], 180))

        StateController.instance.endMainLoop()