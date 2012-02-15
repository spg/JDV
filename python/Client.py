#client
import socket
from network.CommunicationThread import CommunicationThread
from client.ClientDispatcher import ClientDispatcher
from server.actions.StartAction import StartAction
import cPickle

SIZE = 4

class client():
    def __init__(self):
        self._initialiseSocket()
        self.connect('127.0.0.1', 12800)

    def _initialiseSocket(self):
        self.soc1 = socket.socket()
        self.soc2 = socket.socket()

    def connect(self, host, port):
        self.soc1.connect((host, port))
        self.soc1.send('WILL SEND') # telling server we will send data from here
        self.soc2.connect((host, port))
        self.soc2.send('WILL RECV') # telling server we will recieve data from here

    def send(self, data):
        self._msend(self.soc1, data)

    def _msend(self, conn, msg):
        if 999 >= len(msg) > 0:
            conn.send(str(len(msg)))
            if conn.recv(2) == 'OK':
                conn.send(msg)
        else:
            conn.send(str(999))
            if conn.recv(2) == 'OK':
                conn.send(msg[:999])
                self._msend(conn, msg[1000:]) # calling recursive

    def listen(self):
        self.thr = CommunicationThread(self.soc2, ClientDispatcher())
        self.thr.start()

    def stop(self):
        self.thr.stopIt = True
        self._msend(self.soc1, 'bye!!') # for stoping the thread
        self.thr.conn.close()
        self.soc1.close()
        self.soc2.close()

c = client()
c.listen()
c.send(cPickle.dumps(StartAction()))

