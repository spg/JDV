from python.src.robot.pathplanning.pose import Pose

class Robot:
    currentPose = Pose(2078, 225, 90)

    @staticmethod
    def getCurrentPosition():
        return Robot.currentPose.x, Robot.currentPose.y

    @staticmethod
    def getCurrentAngle():
        return Robot.currentPose.theta