# -*- coding: utf-8 -*
import wx
from src.base.Base import Base
from src.base.ui.SetIpDialog import SetIpDialog

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        self._base = Base()

        self._initUi()
        self._bindHandlers()

        self.Show(True)

    def _initUi(self):
        panel = wx.Panel(self, -1)
        self.vroomButton = wx.Button(panel, label="Vrooom!", pos=(300, 300), size=(100, 50))
        self.setIpButton = wx.Button(panel, label="Ip du robot", pos=(300, 400), size=(100,50))
        self._loggingArea = wx.TextCtrl(panel, pos=(275,0), size=(500,250), style=wx.TE_MULTILINE)

    def _bindHandlers(self):
        self.Bind(wx.EVT_BUTTON, self._onVroomClicked, self.vroomButton)
        self.Bind(wx.EVT_BUTTON, self._onSetIpClicked, self.setIpButton)

    def _onVroomClicked(self, event):
        self.spinWheels()

    def _onSetIpClicked(self, event):
        ipdialog = SetIpDialog(self, '10.240.254.168')
        ipdialog.ShowModal()

    def setIp(self, ip):
        self._base.run(ip)

    def spinWheels(self):
        Base.send()

