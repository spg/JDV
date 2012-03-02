import wx
from src.base.ClientLogic import ClientLogic
from src.base.ui.MainWindow import MainWindow

app = wx.App(False)
frame = MainWindow(None, "Robot Picasso")

ClientLogic().run()

app.MainLoop()





