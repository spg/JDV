import wx
from src.base.Base import Base
from src.base.ui.MainWindow import MainWindow

app = wx.App(False)
frame = MainWindow(None, "Robot Picasso")

Base().run()

app.MainLoop()





