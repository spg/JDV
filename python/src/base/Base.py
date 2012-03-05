import cPickle
from Client import client
from src.shared.actions.startrobot import StartRobot

class Base():
    def __init__(self):
        self._client = client()

    def send(self, action):
        self._client.send(cPickle.dumps(action))

    def connectToRobot(self, ip):
        self._client.connect(ip, 12800)
        self._client.listen()
        self.send(StartRobot())
