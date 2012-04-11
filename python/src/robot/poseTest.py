from vision.Camera import Camera

camera = Camera()
try:
    print "Determining current pose..."
    x, y, theta = camera.getCurrentPose()
except:
    print "Couldn't estimate current pose. Please try again"