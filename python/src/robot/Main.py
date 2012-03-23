from python.src.robot.Server import Server
from python.src.robot.robot import Robot

Server(12800)
Server.instance.listen(Robot())