import socket
from ActionDispatcher import ActionDispatcher
from python.src.robot.ai.singletonaccessexception import SingletonAccessException
from python.src.robot.sendevent import SendEvent
from python.src.shared.network.communicationthread import CommunicationThread

class Server():
    instance = None

    def __init__(self):
        if Server.instance:
            raise SingletonAccessException()
        print "sever created"
        Server.instance = self

        self._initializeSocket()
        self._setConnections()
        SendEvent.addHandler(self.send)

    def _initializeSocket(self):
        self.soc = socket.socket()
        self.soc.bind(('', 0))

        print "bound to socket: " + str(self.soc.getsockname()[1])

        self.soc.listen(5)

    def _setConnections(self):
        (c1, a1) = self.soc.accept()
        (c2, a2) = self.soc.accept()
        self.dict = self._setConn(c1, c2)

    def _setConn(self, con1, con2):
        dict = {}
        print 'connexion set'
        state = con1.recv(9)
        print 'state: ', state
        con2.recv(9)
        if state == 'WILL RECV':
            dict['send'] = con1 # server will send data to reciever
            dict['recv'] = con2
        else:
            dict['recv'] = con1 # server will recieve data from sender
            dict['send'] = con2
        return dict

    def listen(self):
        cThread = CommunicationThread(self.dict['recv'], ActionDispatcher())
        cThread.start()

    def send(self, data):
        self._msend(self.dict['send'], data)

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

