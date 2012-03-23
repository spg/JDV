from src.robot.Server import Server
from src.robot.robot import Robot

Server(12800)
Server.instance.listen(Robot())