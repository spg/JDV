import wx
from src.base.ui.MainWindow import MainWindow

class Main():
    def __init__(self):
        self._app = wx.App(False)
        self._frame = MainWindow(None, "Robot Picasso")

    def run(self):
        self._app.MainLoop()

Main().run()





