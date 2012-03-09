from src.robot.ai.singleton import Singleton

class StateController(Singleton):
    def __init__(self, initialState):
        Singleton.__init__(self)
        self.__mainLoopIsOver = False
        self.__currentState = initialState

    def beginMainLopp(self):
        while not self.__mainLoopIsOver:
            self.__currentState.run()

    def setCurrentState(self, state):
        self.__currentState = state

    def endMainLoop(self):
        self.__mainLoopIsOver = True
        print "ended main loop"