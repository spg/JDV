import cPickle
import threading
from Client import client
from src.shared.actions.basetorobot.getlinetra import GetLineTra
from src.shared.actions.basetorobot.startrobot import StartRobot

class Base():
    def __init__(self):
        self._client = client()

    def __send(self, action):
        self._client.send(cPickle.dumps(action))

    def setObstacle(self,x1,y1,x2,y2):
        self.Ox1 = x1
        self.Oy1 = y1
        self.Ox2 = x2
        self.Oy2 = y2

    def connectToRobot(self, ip):
        self._client.connect(ip, 12800)
        self._client.listen()

    def _fetchCurrentPose(self):
        threading.Timer(3, self._fetchCurrentPose).start()
        self.__send(GetLineTra())

    def StartRobot(self):
        self.__send(StartRobot(self.Ox1,self.Oy1,self.Ox2,self.Oy2))

