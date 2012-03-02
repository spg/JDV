import wx
from src.base import ClientLogic
from src.base.ui import MainWindow

app = wx.App(False)
frame = MainWindow(None, "Robot Picasso")

ClientLogic().run()

app.MainLoop()





