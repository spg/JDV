from python.src.robot.pathplanning.Trajectoire import Trajectoire
from python.src.robot.robot import Robot
from python.src.robot.sendevent import SendEvent
from python.src.robot.terrain import Terrain
from python.src.shared.actions.robottobase.sendtrajectoire import SendTrajectoire

class PathBuilder:
    def build(self, destination):
        trajectoire = Trajectoire(Terrain.OBSTACLE_1[0], Terrain.OBSTACLE_1[1], Terrain.OBSTACLE_2[0], Terrain.OBSTACLE_2[1])

        currentRobotPosition = Robot.getCurrentPosition()
        print currentRobotPosition[1]
        print destination[1]

        path = trajectoire.PathFinding(currentRobotPosition[0], currentRobotPosition[1], destination[0], destination[1])

        SendEvent.send(SendTrajectoire(path))

        return path