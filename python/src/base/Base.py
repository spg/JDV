import cPickle
from sched import scheduler
import threading
import time
from Client import client
from src.shared.actions.getpose import GetPose
from src.shared.actions.startrobot import StartRobot

class Base():
    def __init__(self):
        self._client = client()

    def __send(self, action):
        self._client.send(cPickle.dumps(action))

    def connectToRobot(self, ip):
        self._client.connect(ip, 12800)
        self._client.listen()
        self.__send(StartRobot())

        self.__fetchCurrentPose()

    def __fetchCurrentPose(self):
        threading.Timer(10, self.__fetchCurrentPose).start()
        self.__send(GetPose())

