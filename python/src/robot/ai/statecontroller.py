import sys
from python.src.robot.ai.singletonaccessexception import SingletonAccessException

class StateController():
    instance = None

    def __init__( self, initialState ):
        if StateController.instance:
            raise SingletonAccessException()
        print "State Controller created"
        StateController.instance = self

        self.__mainLoopIsOver = False
        self.__currentState = initialState

    def beginMainLopp(self):
        print "beginning main loop"
        self.__mainLoopIsOver = False
        while not self.__mainLoopIsOver:
            print "into main loop"
            self.__currentState.run()

    def setCurrentState(self, state):
        self.__currentState = state

    def endMainLoop(self):
        self.__mainLoopIsOver = True
        print "ended main loop"