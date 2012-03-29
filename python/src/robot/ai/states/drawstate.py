from python.src.robot.arduino.robotmover import RobotMover
from python.src.robot.terrain import Terrain

class DrawState:
    def run(self):
        robotMover = RobotMover()
        robotMover.doSnakeMovement(Terrain.DRAWING_ZONE_CENTER, 270)