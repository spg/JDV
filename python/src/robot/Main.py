from python.src.robot.Server import Server
import atexit

def onExit():
    print "Program exited"

atexit.register(onExit)

Server()
Server.instance.listen()
