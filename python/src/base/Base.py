import cPickle
from src.base.Client import client
from src.shared.actions.StartAction import StartAction

class Base():
    _client = client()
    def run(self):
        print 'hello'
        Base._client.listen()

    @staticmethod
    def send():
        Base._client.send(cPickle.dumps(StartAction()))
        print 'sending...'

