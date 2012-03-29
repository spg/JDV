from python.src.robot.pathplanning.pose import Pose

class Robot:
    currentPose = Pose(207.8, 22.5, 90)

    @staticmethod
    def getCurrentPosition():
        return Robot.currentPose.x, Robot.currentPose.y

    @staticmethod
    def getCurrentAngle():
        return Robot.currentPose.theta