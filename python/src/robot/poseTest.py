from vision.Camera import Camera

camera = Camera()
try:
    print "Determining current pose..."
    x, y, theta = camera.getCurrentPose()
    print "current position = ", x , y
    print "angle = ", theta
except:
    print "Couldn't estimate current pose. Please try again"