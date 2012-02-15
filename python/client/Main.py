import wx
from ui.MainWindow import MainWindow
from ClientLogic import ClientLogic

app = wx.App(False)
frame = MainWindow(None, "Robot Picasso")

ClientLogic().run()

app.MainLoop()





