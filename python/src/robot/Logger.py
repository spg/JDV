from src.robot.sendevent import SendEvent
from src.shared.actions.robottobase.log import Log

class Logger:
    def __init__(self, robot):
        self._robot = robot

    def log(self, message):
        logAction = Log(message)
        SendEvent.send(logAction)
