from python.src.robot.pathplanning.pose import Pose

class Robot:
    currentPose = ()

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