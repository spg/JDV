from python.src.robot.pathplanning.pose import Pose

class Robot:
    currentPose = (207.8, 22.5, 90)

    @staticmethod
    def getCurrentPosition():
        return Robot.currentPose[0], Robot.currentPose[1]

    @staticmethod
    def getCurrentAngle():
        return Robot.currentPose[2]