from python.src.robot.sendevent import SendEvent
from python.src.shared.actions.robottobase.log import Log

class Logger:
    __file = open("logfile", 'w')

    @staticmethod
    def logToFile(message):
        Logger.__file.write("LOG: " + str(message) + '\n')

    @staticmethod
    def logToScreen(message):
        print "LOG: " + str(message)

    @staticmethod
    def logToFileAndScreen(message):
        Logger.logToFile(message)
        Logger.logToScreen(message)

    @staticmethod
    def logToBase(message):
        logAction = Log(message)
        SendEvent.send(logAction)

    @staticmethod
    def logEverywhere(message):
        Logger.logToFile(message)
        Logger.logToScreen(message)
        Logger.logToBase(message)

if __name__ == "__main__":

    Logger.logToFileAndScreen("hello!!!")
    Logger.logToFileAndScreen([(3,4), (6, 7)])
    Logger.logToFileAndScreen("adfkjadsf")
