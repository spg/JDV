import wx

class BaseFrame(wx.Frame):
    def __init__(self, parent, title):
       wx.Frame.__init__(self, parent, title=title, size=(500,250))
       self.initUi()
       self.bindHandlers()
       self.Show(True)

    def initUi(self):
        panel = wx.Panel(self, -1)

        self.textCtrl = wx.TextCtrl(panel, pos=(50, 50), size=(250, 150), style=wx.TE_MULTILINE)

        self.button = wx.Button(panel, label="Click me", pos=(350, 50),size=(100,50))

    def onButtonClicked(self, event):
        self.textCtrl.AppendText("Clicked! ")
        print "clicked!"

    def bindHandlers(self):
        self.Bind(wx.EVT_BUTTON, self.onButtonClicked, self.button)

