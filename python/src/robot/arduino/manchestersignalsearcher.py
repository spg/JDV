import time
from python.src.robot.arduino.arduinointerface import ArduinoInterface
from python.src.robot.arduino.manchestersignalinterpreter import ManchesterSignalInterpreter
from python.src.robot.pathplanning.robotmover import RobotMover
from python.src.robot.robot import Robot
from python.src.robot.terrain import Terrain

class ManchesterSignalSearcher:
    def __init__(self):
        self.arduinoInterface = ArduinoInterface.getInstance()
        self.manchesterSignalInterpreter = ManchesterSignalInterpreter()

    def searchSignal(self):
        robotMover = RobotMover()
        robotMover.doSnakeMovement(Terrain.DRAWING_ZONE_NORTH_EAST_CORNER_INNER, 180)

        distance, signal = self.__doSignalSearch('SS.')

        self.__adjustPosition(distance, 4)

        signalPosition = Robot.getCurrentPosition()

        self.__moveToSecondCorner()

        distance, signal = self.__doSignalSearch('SB.')

        self.__adjustPosition(distance, -4)

        interpretedSignal = self.manchesterSignalInterpreter.interpretSignal(signal)

        return interpretedSignal, signalPosition

    def __doSignalSearch(self, method):
        print "searching signal..."
        self.arduinoInterface.write(method)
        time.sleep(0.2)
        self.arduinoInterface.checkIfOperationIsOver()
        signalAndDistance = self.arduinoInterface.readLine()

        print "signal and distance: " + str(signalAndDistance)

        signal = signalAndDistance[0:7]
        distance = signalAndDistance[8:]

        print "distance traveled: " + str(distance)
        print "signal: " + str(signal)

        return distance, signal

    def __moveToSecondCorner(self):
        robotMover = RobotMover()
        robotMover.doSnakeMovement(Terrain.DRAWING_ZONE_SOUTH_EAST_CORNER_INNER, 0)

    def __adjustPosition(self, distance, verticalDrift):
        ancientPose = Robot.getCurrentPose()

        newPose = (ancientPose[0] - (int(distance)/10), ancientPose[1] + verticalDrift, ancientPose[2])

        Robot.setCurrentPose(newPose)

    def doSimpleSignalDecoding(self):
        self.arduinoInterface.write('SD.')

        self.arduinoInterface.checkIfOperationIsOver()

        signal = self.arduinoInterface.readLine()
        interpretedSignal = self.manchesterSignalInterpreter.interpretSignal(signal)

        return interpretedSignal