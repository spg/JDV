from python.src.robot.ai.statecontroller import StateController
from python.src.robot.ai.states.searchlocation import SearchLocation
from python.src.robot.ai.states.state import State
from python.src.robot.pathplanning.Trajectoire import Trajectoire
from python.src.robot.sendevent import SendEvent
from python.src.robot.terrain import Terrain
from python.src.shared.actions.robottobase.senddesssin import SendDessin
from python.src.shared.actions.robottobase.sendtrajectoire import SendTrajectoire

class BeginState(State):
    def __init__(self, obstacle1, obstacle2):
        Terrain.OBSTACLE_1 = obstacle1
        Terrain.OBSTACLE_2 = obstacle2

    def run(self):
        print "begin state running..."

        trajectoire = Trajectoire(Terrain.OBSTACLE_1[0], Terrain.OBSTACLE_1[1], Terrain.OBSTACLE_2[0], Terrain.OBSTACLE_2[1])
        path = trajectoire.PathFinding(350, 210, 50, 210)

        SendEvent.send(SendTrajectoire(path))

        #SendEvent.send(SendDessin([(10,10), (30,30), (40,20), (30,10), (50,20), (30, 50), (10,10)]))
        #StateController.instance.setCurrentState(SearchLocation())