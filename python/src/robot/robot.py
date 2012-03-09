import cPickle
from src.robot.Server import Server
from src.robot.ai.advancestate import AdvanceState
from src.robot.ai.statecontroller import StateController

class Robot:
    _server = Server(12800)

    def startLIstening(self):
        Robot._server.listen(self)

    def send(self, action):
        Robot._server.send(cPickle.dumps(action))

    def activate(self):
        stateController = StateController(AdvanceState())
        stateController.beginMainLopp()