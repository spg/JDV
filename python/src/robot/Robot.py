from src.robot.Server import Server

class Robot:
    def __init__(self):
        self.server = Server(12800)

    def activate(self):
        self.server.listen()