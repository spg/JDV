import socket
from ActionDispatcher import ActionDispatcher
from src.shared.network.communicationthread import CommunicationThread

class Server():
    def __init__(self, port):
        self.port = port

        self._initializeSocket()
        self._setConnections()

    def _initializeSocket(self):
        self.soc = socket.socket()
        self.soc.bind(('',self.port))
        self.soc.listen(5)

    def _setConnections(self):
        (c1,a1) = self.soc.accept()
        (c2,a2) = self.soc.accept()
        self.dict = self._setConn(c1,c2)

    def _setConn(self, con1, con2):
        dict={}
        print 'connexion set'
        state = con1.recv(9)
        print 'state: ', state
        con2.recv(9)
        if state =='WILL RECV':
            dict['send'] = con1 # server will send data to reciever
            dict['recv'] = con2
        else:
            dict['recv'] = con1 # server will recieve data from sender
            dict['send'] = con2
        return dict

    def listen(self, robot):
        cThread = CommunicationThread(self.dict['recv'], ActionDispatcher(robot))
        cThread.start()

    def send(self, data):
        print 'sending back to base'
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
                self._msend(conn,msg[1000:]) # calling recursive

