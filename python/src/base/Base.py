import cPickle
from src.base.Client import client
from src.shared.actions.StartAction import StartAction

class Base():
    _client = client()
    def run(self, robotIp):
        print 'hello'
        Base._client.connect(robotIp, 12800)
        Base._client.listen()

    @staticmethod
    def send():
        Base._client.send(cPickle.dumps(StartAction()))
        print 'sending...'

