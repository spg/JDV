from python.src.robot.vision.Camera import Camera

cam = Camera()

print "Extracting points with camera..."
drawingCountour = cam.getDrawingContour()

print str(drawingCountour)