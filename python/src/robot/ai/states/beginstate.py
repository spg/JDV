from __future__ import division

import time
from python.src.robot.ai.statecontroller import StateController
from python.src.robot.ai.states.state import State
from python.src.robot.arduino.manchestersignalinterpreter import ManchesterSignalInterpreter
from python.src.robot.arduino.prehensorcontroller import PrehensorController
from python.src.robot.arduino.robotmover import RobotMover
from python.src.robot.robot import Robot
from python.src.robot.sendevent import SendEvent
from python.src.robot.terrain import Terrain
from python.src.robot.util.pointscloudscaler import PointsCloudOperations
from python.src.robot.vision.Camera import Camera

from python.src.shared.actions.robottobase.senddesssin import SendDessin

class BeginState(State):
    def __init__(self, obstacle1, obstacle2):
        Terrain.OBSTACLE_1 = obstacle1
        Terrain.OBSTACLE_2 = obstacle2

        print "obstacle 1: " + str(obstacle1)
        print "obstacle 2: " + str(obstacle2)

        self.robotMover = RobotMover()

    def run(self):
        Robot.setCurrentPose((Terrain.DRAWING_ZONE_NORTH_EAST_CORNER_INNER[0], Terrain.DRAWING_ZONE_NORTH_EAST_CORNER_INNER[1], 180))

        print "running..."

        print "doing snake movement 1..."

        #self.robotMover.doSnakeMovement(Terrain.DRAWING_ZONE_NORTH_EAST_CORNER, 180)
        print "snake movement 1 over!"

        signalInterpreter = ManchesterSignalInterpreter()

        signalInterpreter.searchSignal()

        StateController.instance.endMainLoop()

    def doDrawing(self):

        print "Creating camera..."
        cam = Camera()

        print "Extracting points..."
        drawingCountoursFound = False

        drawingCountour = []

        while not drawingCountoursFound:
            try:
                drawingCountour = cam.getDrawingContour()
                drawingCountoursFound = True
            except ValueError:
                pass

        points = drawingCountour[0]
        size = drawingCountour[1]

        print "Extracted points: "
        print points
        print "Size: "
        print size

        drawingZoneSide = 60 # dimension in CM
        scaleFactor = drawingZoneSide / size
        
        scaledPoints = PointsCloudOperations.scale(points, scaleFactor)

        SendEvent.send(SendDessin(scaledPoints))

        movedPoints = PointsCloudOperations.move(scaledPoints, 144.8, 25.5)

        print "going to first drawing point"
        self.robotMover.doSnakeMovement(movedPoints[0], 270)
        print "arrived at first drawing point!"

        prehensorController = PrehensorController()
        prehensorController.dropPrehensor()

        movedPoints.append(movedPoints[0]) # this is to close the figure

        self.robotMover.doShuffleMovement(movedPoints)

        prehensorController.raisePrehensor()
