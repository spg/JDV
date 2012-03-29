from python.src.robot.ai.statecontroller import StateController
from python.src.robot.ai.states.captureimagestate import CaptureImageState
from python.src.robot.ai.states.state import State
from python.src.robot.arduino.robotmover import RobotMover
from python.src.robot.pathplanning.Trajectoire import Trajectoire
from python.src.robot.sendevent import SendEvent
from python.src.robot.terrain import Terrain
from python.src.shared.actions.robottobase.sendtrajectoire import SendTrajectoire

class BeginState(State):
    def __init__(self, obstacle1, obstacle2):
        Terrain.OBSTACLE_1 = obstacle1
        Terrain.OBSTACLE_2 = obstacle2

    def run(self):
        trajectoire = Trajectoire(Terrain.OBSTACLE_1[0], Terrain.OBSTACLE_1[1], Terrain.OBSTACLE_2[0], Terrain.OBSTACLE_2[1])

        path = trajectoire.PathFinding(200, 160 ,2078 , 885)

        SendEvent.send(SendTrajectoire(path))
        #robotMover = RobotMover()
        #robotMover.doSnakeMovement(Terrain.FIGURE_5_FACE, 180)

        #StateController.instance.setCurrentState(CaptureImageState())