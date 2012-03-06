# -*- coding: utf-8 -*
import time
import wx
from src.base.Base import Base
from src.base.logevent import LogEvent

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        self.__base = Base()

        self.__initUi()
        self.__bindHandlers()

        self.Show(True)

        LogEvent.addHandler(self.__logReceived)

    def __initUi(self):
        panel = wx.Panel(self)
        self.__connectionButton = wx.Button(panel, label="Se connecter au: ", pos=(500, 300), size=(130, 50))
        self.__loggingArea = wx.TextCtrl(panel, pos=(275,0), size=(500,250), style=wx.TE_MULTILINE)
        self.__ipTextCtrl = wx.TextCtrl(panel, value='10.240.254.168', pos=(650, 300), size=(100, 50))

    def __bindHandlers(self):
        self.Bind(wx.EVT_BUTTON, self.__onConnectButtonClicked, self.__connectionButton)

    def __onConnectButtonClicked(self, event):
        self.__connectionButton.Disable()
        self.__ipTextCtrl.Disable()

        self.__base.connectToRobot(self.__ipTextCtrl.GetValue())

    def __logReceived(self, message):
        wx.CallAfter(self.__printToLoggingArea, message)

    def __printToLoggingArea(self, message):
        currentTime = time.strftime("%H:%M:%S", time.localtime())
        self.__loggingArea.AppendText(currentTime + ' : ' + message +'\n')