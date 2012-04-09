import time
from python.src.robot.arduino.arduinointerface import ArduinoInterface
from python.src.robot.arduino.manchestersignalinterpreter import ManchesterSignalInterpreter
from python.src.robot.arduino.robotmover import RobotMover
from python.src.robot.robot import Robot
from python.src.robot.terrain import Terrain

class ManchesterSignalSearcher:
    def __init__(self):
        self.arduinoInterface = ArduinoInterface.getInstance()
        self.manchesterSignalInterpreter = ManchesterSignalInterpreter()

    def searchSignal(self):
        distance, signal = self.__doSignalSearch('SS.')

        self.__moveToSecondCorner(distance)

        distance, signal = self.__doSignalSearch('SB.')

        interpretedSignal = self.manchesterSignalInterpreter.interpretSignal(signal)

        return interpretedSignal

    def __doSignalSearch(self, method):
        print "searching signal..."
        ser = self.arduinoInterface.connect()
        ser.write(method)
        time.sleep(0.2)
        self.arduinoInterface.checkIfOperationIsOver(ser)
        signalAndDistance = self.arduinoInterface.readLine(ser)

        print "signal and distance: " + str(signalAndDistance)

        signal = signalAndDistance[0:7]
        distance = signalAndDistance[8:]

        print "distance traveled: " + str(distance)
        print "signal: " + str(signal)

        return distance, signal

    def __moveToSecondCorner(self, distanceTraveled):
        ancientPose = Robot.getCurrentPose()

        verticalDrift = 4 #in cm

        newPose = (ancientPose[0] - (int(distanceTraveled)/10), ancientPose[1] + verticalDrift, ancientPose[2])

        Robot.setCurrentPose(newPose)

        robotMover = RobotMover()
        robotMover.doSnakeMovement(Terrain.DRAWING_ZONE_SOUTH_EAST_CORNER_INNER, 0)