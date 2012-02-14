import wx
from ui.MainWindow import MainWindow

app = wx.App(False)
frame = MainWindow(None, "Robot Picasso")
app.MainLoop()
