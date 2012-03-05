import cPickle
from src.robot.Server import Server

class Robot:
    _server = Server(12800)

    def activate(self):
        Robot._server.listen()

    @staticmethod
    def send(action):
        Robot._server.send(cPickle.dumps(action))