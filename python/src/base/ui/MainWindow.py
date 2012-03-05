# -*- coding: utf-8 -*
import time
import wx
from src.base.Base import Base
from src.base.logevent import LogEvent
from src.base.ui.SetIpDialog import SetIpDialog
from src.shared.actions.startrobot import StartRobot

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        self.__base = Base()

        self.__initUi()
        self.__bindHandlers()
        self.__defaultIp = 'localhost'

        self.Show(True)

        LogEvent.addHandler(self.__logReceived)

    def __initUi(self):
        panel = wx.Panel(self, -1)
        self.__connectionButton = wx.Button(panel, label="Connecter au robot!", pos=(300, 300), size=(100, 50))
        self.__setIpButton = wx.Button(panel, label="Ip du robot", pos=(300, 400), size=(100,50))
        self.__loggingArea = wx.TextCtrl(panel, pos=(275,0), size=(500,250), style=wx.TE_MULTILINE)

    def __bindHandlers(self):
        self.Bind(wx.EVT_BUTTON, self.__onConnectButtonClicked, self.__connectionButton)
        self.Bind(wx.EVT_BUTTON, self.__onSetIpClicked, self.__setIpButton)

    def __onConnectButtonClicked(self, event):
        self.__disableConnectionButtons()
        self.__base.connectToRobot(self.__defaultIp)

    def __disableConnectionButtons(self):
        self.__connectionButton.Disable()
        self.__setIpButton.Disable()

    def __onSetIpClicked(self, event):
        ipdialog = SetIpDialog(self, 'localhost')
        ipdialog.ShowModal()

    def setIp(self, ip):
        self.__disableConnectionButtons()
        self.__base.connectToRobot(ip)

    def __logReceived(self, message):
        print "Time (24hr) :", time.strftime("%H:%M:%S", time.localtime())
        self.__loggingArea.AppendText(message +'\n')

