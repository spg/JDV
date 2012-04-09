from __future__ import division

from python.src.robot.ai.statecontroller import StateController
from python.src.robot.arduino.captorscontroller import CaptorsController
from python.src.robot.arduino.manchestersignalinterpreter import ManchesterSignalInterpreter
from python.src.robot.arduino.manchestersignalsearcher import ManchesterSignalSearcher
from python.src.robot.arduino.prehensorcontroller import PrehensorController
from python.src.robot.arduino.robotmover import RobotMover
from python.src.robot.robot import Robot
from python.src.robot.sendevent import SendEvent
from python.src.robot.terrain import Terrain
from python.src.robot.util.imagepointstransformer import ImagePointsTransformer
from python.src.robot.util.pointscloudscaler import PointsCloudOperations
from python.src.robot.vision.Camera import Camera
from python.src.shared.actions.robottobase.sendConfirm import SendConfirm
from python.src.shared.actions.robottobase.sendEnd import SendEnd

from python.src.shared.actions.robottobase.senddesssin import SendDessin

class BeginState:
    def __init__(self, obstacle1, obstacle2):
        Terrain.OBSTACLE_1 = obstacle1
        Terrain.OBSTACLE_2 = obstacle2

        print "obstacle 1: " + str(obstacle1)
        print "obstacle 2: " + str(obstacle2)

        SendEvent.send(SendConfirm())

        self.robotMover = RobotMover()
        self.signalSearcher = ManchesterSignalSearcher()
        self.captorsController = CaptorsController()
        self.imagePointsTransformer = ImagePointsTransformer()

    def run(self):
        self.__acquireCurrentPose()

        interpretedSignal = self.signalSearcher.searchSignal()

        print "interpreted signal: " + str(interpretedSignal)

        figureId = interpretedSignal[0]
        orientation = interpretedSignal[1]
        scale = interpretedSignal[2]

        self.__goToProperImageForScanning(figureId)

        self.__doDrawing(orientation, scale)

        SendEvent.send(SendEnd())
        StateController.instance.endMainLoop()
        return

    def __acquireCurrentPose(self):
        print "Doing zignage..."
        self.captorsController.Zing()

        Robot.setCurrentPose((Terrain.DRAWING_ZONE_CENTER[0], Terrain.DRAWING_ZONE_CENTER[1], 90))

        print "Current robot pose is: " + str(Robot.getCurrentPose())

    def __goToProperImageForScanning(self, imageId):
        self.robotMover.doSnakeMovement(Terrain.AR_TAG_SOUTH_FACE, 90)

        self.__acquireCurrentPose()


        if imageId == ManchesterSignalInterpreter.FIGURE_0:
            print "going to figure 0"
            self.robotMover.doSnakeMovement(Terrain.FIGURE_0_FACE, 90)
        elif imageId == ManchesterSignalInterpreter.FIGURE_1:
            print "going to figure 1"
            self.robotMover.doSnakeMovement(Terrain.FIGURE_1_FACE, 90)
        elif imageId == ManchesterSignalInterpreter.FIGURE_2:
            print "going to figure 2"
            self.robotMover.doSnakeMovement(Terrain.FIGURE_2_FACE, 180)
        elif imageId == ManchesterSignalInterpreter.FIGURE_3:
            print "going to figure 3"
            self.robotMover.doSnakeMovement(Terrain.FIGURE_3_FACE, 180)
        elif imageId == ManchesterSignalInterpreter.FIGURE_4:
            print "going to figure 4"
            self.robotMover.doSnakeMovement(Terrain.FIGURE_4_FACE, 180)
        elif imageId == ManchesterSignalInterpreter.FIGURE_5:
            print "going to figure 5"
            self.robotMover.doSnakeMovement(Terrain.FIGURE_5_FACE, 180)
        elif imageId == ManchesterSignalInterpreter.FIGURE_6:
            print "going to figure 6"
            self.robotMover.doSnakeMovement(Terrain.FIGURE_6_FACE, 270)
        elif imageId == ManchesterSignalInterpreter.FIGURE_7:
            print "going to figure 7"
            self.robotMover.doSnakeMovement(Terrain.FIGURE_7_FACE, 270)

    def __doDrawing(self, orientation, scale):
        cam = Camera()

        print "Extracting points with camera..."
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

        print points
        print size

        pointsToDraw = self.imagePointsTransformer.transform(points, orientation, scale)

        SendEvent.send(SendDessin(pointsToDraw))

        movedPoints = PointsCloudOperations.move(pointsToDraw, 144.8, 25.5)

        print "going to first drawing point"
        self.robotMover.doSnakeMovement(movedPoints[0], 270)
        print "arrived at first drawing point!"

        prehensorController = PrehensorController()
        prehensorController.dropPrehensor()

        movedPoints.append(movedPoints[0]) # this is to close the figure

        self.robotMover.doShuffleMovement(movedPoints)

        prehensorController.raisePrehensor()
