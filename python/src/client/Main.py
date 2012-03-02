import wx
from src.client import ClientLogic
from src.client.ui import MainWindow

app = wx.App(False)
frame = MainWindow(None, "Robot Picasso")

ClientLogic().run()

app.MainLoop()





