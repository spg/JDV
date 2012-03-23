from src.robot.ai.singletonaccessexception import SingletonAccessException

class Singleton:
    instance = None
    def __init__( self ):
        if Singleton.instance:
            raise SingletonAccessException()
        print "singleton created"
        Singleton.instance = self