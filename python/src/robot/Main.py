from python.src.robot.Server import Server
import atexit

def onExit():
    print "bonjourrrrrrrrr"

atexit.register(onExit)

Server()
Server.instance.listen()
