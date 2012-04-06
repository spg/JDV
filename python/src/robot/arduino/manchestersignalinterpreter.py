from __future__ import division

import time
from python.src.robot.arduino.arduinointerface import ArduinoInterface
from python.src.robot.arduino.robotmover import RobotMover
from python.src.robot.robot import Robot
from python.src.robot.terrain import Terrain

class ManchesterSignalInterpreter:
    FIGURE_0 = "000"
    FIGURE_1 = "001"
    FIGURE_2 = "010"
    FIGURE_3 = "011"
    FIGURE_4 = "100"
    FIGURE_5 = "101"
    FIGURE_6 = "110"
    FIGURE_7 = "111"

    NORTH = "00"
    EAST = "01"
    SOUTH = "10"
    WEST = "11"

    FACTOR_2 = "0"
    FACTOR_4 = "1"

    def __init__(self):
        self.arduinoInterface = ArduinoInterface.getInstance()

    def searchSignal(self):
        distanceTraveled = self.__doSignalSearch()

        self.decodeSignal()

        self.__moveToSecondCorner(distanceTraveled)

        self.__doSignalSearch()

        self.decodeSignal()

    def __doSignalSearch(self):
        print "searching signal..."
        ser = self.arduinoInterface.connect()
        ser.write('SS.')
        time.sleep(0.2)
        self.arduinoInterface.checkIfOperationIsOver(ser)
        distanceTraveled = self.arduinoInterface.readLine(ser)

        print "distance traveled: " + str(distanceTraveled)

        return distanceTraveled

    def __moveToSecondCorner(self, distanceTraveled):
        ancientPose = Robot.getCurrentPose()

        newPose = (ancientPose[0] - (int(distanceTraveled)/10), ancientPose[1], ancientPose[0])

        Robot.setCurrentPose(newPose)

        robotMover = RobotMover()
        robotMover.doSnakeMovement(Terrain.DRAWING_ZONE_SOUTH_EAST_CORNER, 0)

    def decodeSignal(self):
        print "decoding signal..."
        ser = self.arduinoInterface.connect()

        ser.write('SD.')

        time.sleep(0.2)

        self.arduinoInterface.checkIfOperationIsOver(ser)

        rawManchestSignal = self.arduinoInterface.readLine(ser)

        print "manchesterCode: " + str(rawManchestSignal[0:7])

    def interpretSignal(self, signal):
        figure = signal[0:3]
        orientation = signal[3:5]
        factor = signal[5]

        interpretedFigure = self.__interpretFigure(figure)
        interpretedOrientation = self.__interpreOrientation(orientation)
        interpretedFactor = self.__interpretFactor(factor)

        return interpretedFigure, interpretedOrientation, interpretedFactor

    def __interpretFigure(self, figure):
        interpretedFigure = ""

        if figure == ManchesterSignalInterpreter.FIGURE_0:
            interpretedFigure = ManchesterSignalInterpreter.FIGURE_0
        elif figure == ManchesterSignalInterpreter.FIGURE_1:
            interpretedFigure=  ManchesterSignalInterpreter.FIGURE_1
        elif figure == ManchesterSignalInterpreter.FIGURE_2:
            interpretedFigure = ManchesterSignalInterpreter.FIGURE_2
        elif figure == ManchesterSignalInterpreter.FIGURE_3:
            interpretedFigure = ManchesterSignalInterpreter.FIGURE_3
        elif figure == ManchesterSignalInterpreter.FIGURE_4:
            interpretedFigure = ManchesterSignalInterpreter.FIGURE_4
        elif figure == ManchesterSignalInterpreter.FIGURE_5:
            interpretedFigure = ManchesterSignalInterpreter.FIGURE_5
        elif figure == ManchesterSignalInterpreter.FIGURE_6:
            interpretedFigure = ManchesterSignalInterpreter.FIGURE_6
        elif figure == ManchesterSignalInterpreter.FIGURE_7:
            interpretedFigure = ManchesterSignalInterpreter.FIGURE_7

        return interpretedFigure

    def __interpreOrientation(self, orientation):
        interpretedOrientation = ""

        if orientation == ManchesterSignalInterpreter.NORTH:
            interpretedOrientation = ManchesterSignalInterpreter.NORTH
        elif orientation == ManchesterSignalInterpreter.SOUTH:
            interpretedOrientation=  ManchesterSignalInterpreter.SOUTH
        elif orientation == ManchesterSignalInterpreter.EAST:
            interpretedOrientation = ManchesterSignalInterpreter.EAST
        elif orientation == ManchesterSignalInterpreter.WEST:
            interpretedOrientation = ManchesterSignalInterpreter.WEST

        return interpretedOrientation

    def __interpretFactor(self, factor):
        interpretedFactor = ""

        if factor == ManchesterSignalInterpreter.FACTOR_2:
            interpretedFactor = ManchesterSignalInterpreter.FACTOR_2
        elif factor == ManchesterSignalInterpreter.FACTOR_4:
            interpretedFactor=  ManchesterSignalInterpreter.FACTOR_4

        return interpretedFactor
