import cPickle
from src.base.Client import client
from src.shared.actions.StartAction import StartAction

class ClientLogic():
    _client = client()
    def run(self):
        print 'hello'
        ClientLogic._client.listen()

    @staticmethod
    def send():
        ClientLogic._client.send(cPickle.dumps(StartAction()))
        print 'sending...'

