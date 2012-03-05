from Robot import Robot
from src.shared.actions.LogMessage import LogMessage

class Logger():
    @staticmethod
    def log(self, message):
        logAction = LogMessage(message)
        Robot.send(logAction)
