# -*- coding: utf-8 -*
import wx
from src.client import ClientLogic

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 400))
        self._initUi()
        self._bindHandlers()
        self.Show(True)

    def _initUi(self):
        panel = wx.Panel(self, -1)

        self.vroomButton = wx.Button(panel, label="Vrooom!", pos=(300, 50), size=(100, 50))

    def _bindHandlers(self):
        self.Bind(wx.EVT_BUTTON, self._onVroomClicked, self.vroomButton)

    def _onVroomClicked(self, event):
        self.spinWheels()

    def spinWheels(self):
        ClientLogic.ClientLogic.send()

