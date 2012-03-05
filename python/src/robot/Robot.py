import cPickle
from src.robot.Server import Server

class Robot:
    _server = Server(12800)

    def activate(self):
        Robot._server.listen(self)

    def send(self, action):
        Robot._server.send(cPickle.dumps(action))