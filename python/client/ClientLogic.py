import cPickle
from client.Client import client
from server.actions.StartAction import StartAction

class ClientLogic():
    _client = client()
    def run(self):
        print 'hello'
        ClientLogic._client.listen()

    @staticmethod
    def send():
        ClientLogic._client.send(cPickle.dumps(StartAction()))
        print 'sending...'

