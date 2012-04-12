from vision.Camera import Camera

camera = Camera()
print "Determining current pose..."
x, y, theta = camera.getCurrentPose()
print "current position = ", x , y
print "angle = ", theta
print "Couldn't estimate current pose. Please try again"