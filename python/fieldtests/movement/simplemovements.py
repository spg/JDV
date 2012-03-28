from python.src.robot.arduino.positioncontroller import PositionController

positionController = PositionController()
positionController.advance(10)
positionController.rotate(90)
positionController.advance(10)
positionController.rotate(-90)
positionController.advance(20)
positionController.rotate(180)