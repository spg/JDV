import wx
from ui.BaseFrame import BaseFrame

app = wx.App(False)
frame = BaseFrame(None, "Smalle editor")
app.MainLoop()
