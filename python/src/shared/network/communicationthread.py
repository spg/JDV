import threading

SIZE = 4

class CommunicationThread(threading.Thread):
    def __init__(self,c, dispatcher):
        threading.Thread.__init__(self)
        self.conn = c
        self.stopIt=False
        self.dispatcher = dispatcher

    def mrecv(self):
        data = self.conn.recv(SIZE)
        self.conn.send('OK')
        msg = self.conn.recv(int(data))
        return msg

    def run(self):
        while not self.stopIt:
            msg = self.mrecv()
            self.dispatcher.dispatch(msg)