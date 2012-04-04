from python.src.robot.sendevent import SendEvent
from python.src.shared.actions.robottobase.sendpose import SendPose

class Robot:
    currentPose = (0,0,0)

    @staticmethod
    def getCurrentPosition():
        return Robot.currentPose[0], Robot.currentPose[1]

    @staticmethod
    def getCurrentAngle():
        return Robot.currentPose[2]

    @staticmethod
    def getCurrentPose():
        return Robot.currentPose

    @staticmethod
    def setCurrentPose(pose):
        Robot.currentPose = pose
        SendEvent.send(SendPose(pose[0], pose[1], pose[2]))