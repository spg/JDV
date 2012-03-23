#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode wxPython tutorial

This program draws a line on the
frame window after a while

author: Jan Bodnar
website: zetcode.com
last edited: November 2010
"""
import math
import time
import wx
from src.base.ui.Trajectoire import  Trajectoire
from src.base.Base import Base
from src.base.logevent import LogEvent
from src.base.poseevent import PoseEventvent
from src.base.trajectoireevent import TrajectoireEvent
from src.base.dessinevent import DessinEvent
from src.base.ui.Obstacle import  Obstacle
from src.shared.actions.basetorobot.startrobot import StartRobot


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent, title=title,
            size=(700, 550))
        self.panel = wx.Panel(self, -1)
        self.__countAction = 0
        self.__Action = True
        self.__robotx = 50
        self.__roboty = 50
        self.__angleActuelle = 0
        self.__coordx1 = -1
        self.__coordy1 = -1
        self.__coordx2 = 1
        self.__coordy2 = -1
        self.__base = Base()
        wx.FutureCall(2000, self.__DrawLine)
        self.Centre()
        self.Show()
        LogEvent.addHandler(self.__logReceived)
        PoseEventvent.addHandler(self.__PoseReceived)
        TrajectoireEvent.addHandler(self.__TrajectoireReceived)
        DessinEvent.addHandler(self.__DessinReceived)


    def __bindHandlers(self):
        self.Bind(wx.EVT_BUTTON, self.__onButtonClicked, self.__button)
        self.Bind(wx.EVT_BUTTON, self.__onAfficheClicked, self.__Affiche)
        self.Bind(wx.EVT_BUTTON, self.__onConnectButtonClicked, self.__connectionButton)


    def __DrawLine(self):
        #option de décalage

        self.__offset = 10
        self.dc = wx.ClientDC(self.panel)
        # La zone de jeux
        self.dc.SetBrush(wx.Brush('#ffffff'))
        self.dc.DrawRectangle(0 + self.__offset, 0 + self.__offset, 220, 460)
        self.dc.DrawRectangle(230 + self.__offset, 0 + self.__offset, 242, 242)
        # Aire de dessin
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle(44 + self.__offset, 228 + self.__offset, 133, 133)
        self.dc.SetBrush(wx.Brush('#ffffff'))
        self.dc.DrawRectangle(50 + self.__offset, 234 + self.__offset, 121, 121)
        #ligne rouge
        self.dc.SetBrush(wx.Brush('#ff0000'))
        self.dc.DrawRectangle(0 + self.__offset, 158 + self.__offset, 220, 4)
        # Point d'arriver pour les dessins
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle(20 + self.__offset, 10 + self.__offset, 5, 5)
        self.dc.DrawRectangle(70 + self.__offset, 10 + self.__offset, 5, 5)
        self.dc.DrawRectangle(130 + self.__offset, 10 + self.__offset, 5, 5)
        self.dc.DrawRectangle(190 + self.__offset, 10 + self.__offset, 5, 5)
        self.dc.DrawRectangle(20 + self.__offset, 30 + self.__offset, 5, 5)
        self.dc.DrawRectangle(20 + self.__offset, 60 + self.__offset, 5, 5)
        self.dc.DrawRectangle(190 + self.__offset, 30 + self.__offset, 5, 5)
        self.dc.DrawRectangle(190 + self.__offset, 60 + self.__offset, 5, 5)
        # Point d'arriver pour la zone de  dessins
        self.dc.DrawRectangle(55 + self.__offset, 240 + self.__offset, 5, 5)
        # Met le robot sur la zone
        self.dc.SetBrush(wx.Brush('#ff0000'))
        self.__xL1 = self.__robotx + (10 * self.__coordx1)
        self.__xL2 = self.__robotx + (10 * self.__coordx2)
        self.__yL1 = self.__roboty + (10 * self.__coordy1)
        self.__yL2 = self.__roboty + (10 * self.__coordy2)
        self.dc.DrawLine(self.__robotx, self.__roboty, self.__xL1, self.__yL1)
        self.dc.DrawLine(self.__robotx, self.__roboty, self.__xL2, self.__yL2)
        self.dc.DrawLine(self.__xL2, self.__yL2, self.__xL1, self.__yL1)
        if self.__Action:
            self.__Action = False
            self.__button = wx.Button(self.panel, label="Obstacle", pos=(500, 10), size=(100, 25))
            self.__Affiche = wx.Button(self.panel, label="Affiche", pos=(500, 50), size=(100, 25))
            self.__connectionButton = wx.Button(self.panel, label="Se connecter au: ", pos=(500, 90), size=(130, 25))
            self.__loggingArea = wx.TextCtrl(self.panel, pos=(250, 260), size=(200, 200), style=wx.TE_MULTILINE)
            self.__ipTextCtrl = wx.TextCtrl(self.panel, value='localhost', pos=(500, 140), size=(100, 25))
            self.__bindHandlers()

    def __onConnectButtonClicked(self, event):
        self.__connectionButton.Disable()
        self.__ipTextCtrl.Disable()
        self.__base.connectToRobot(self.__ipTextCtrl.GetValue())
        self.__base.setObstacle(100, 100, 100, 100)
        self.__base.StartRobot()
        self.__base._fetchCurrentPose()


    def __logReceived(self, message):
        wx.CallAfter(self.__printToLoggingArea, message)

    def __PoseReceived(self, message):
        self.dc.Clear()
        Angle = message.theta
        self.__RotationTriangle(Angle)
        self.robotx = message.x
        self.roboty = message.y
        self.__DrawLine()

    def __DessinReceived(self, message):
        self.AfficherDessin(self, message.listex, message.listeY, message.LongueurListe)


    def __TrajectoireReceived(self, message):
        self.AfficherTrajectoire(message.liste)

    def __AfficherTrajectoire(self, liste):
        i = 0
        Depart = True
        x = x1 = y = y1 = 0
        for  x, y  in liste :
            if Depart == True :
                Depart = False
            else:
                self.dc.DrawLine(x1, y1, x, y)
            x1 = x
            y1 = y



    def __AfficherDessin(self, listeX, listeY, LongueurListe):
        while i < LongueurListe - 1:
            self.dc.DrawLine(listeX[i] + 240, listeY[i] + 10, listeX[i + 1] + 240, listeY[i + 1] + 10)
            i = i + 1

    def __printToLoggingArea(self, message):
        currentTime = time.strftime("%H:%M:%S", time.localtime())
        self.__loggingArea.AppendText(currentTime + ' : ' + message + '\n')

    def __RotationTriangle(self, angle):
        x = ((self.robotx - self.xL1 ) / 10)
        y = ((self.roboty - self.yL1) / 10)
        _angle = angle - self._angleActuelle
        self.__angleActuelle = self._angleActuelle + _angle
        self.__coordx1 = 0 - (x * math.cos(math.radians(_angle)) - (y * math.sin(math.radians(_angle))))
        self.__coordy1 = 0 - (x * math.sin(math.radians(_angle)) + (y * math.cos(math.radians(_angle))))
        x1 = ((self.__robotx - self.__xL2) / 10)
        y1 = ((self.__roboty - self.__yL2) / 10)
        self.__coordx2 = 0 - (x1 * math.cos(math.radians(_angle)) - (y1 * math.sin(math.radians(_angle))))
        self.__coordy2 = 0 - (x1 * math.sin(math.radians(_angle)) + (y1 * math.cos(math.radians(_angle))))

    def __onButtonClicked(self, event):
        O = Obstacle()
        O.Show()

    def __onAfficheClicked(self, event):
        #Affiche les obstacle
        #self.x1=self.O.getx1()+self.d
        #self.x2=self.O.getx2()+self.d
        #self.y1=self.O.gety1()+self.d
        #self.y2=self.O.gety2()+self.d
        #Valeur par default pour bu de test
        self.__x1 = 140 + self.__offset
        self.__y1 = 250 + self.__offset
        self.__x2 = 140 + self.__offset
        self.__y2 = 150 + self.__offset
        #Affichage des obstacle
        self.dc.SetBrush(wx.Brush('#000000'))
        self.dc.DrawRectangle(self.__x1, self.__y1, 20, 20)
        self.dc.DrawRectangle(self.__x2, self.__y2, 20, 20)
        #Affichage des noeuds des obstacles
        #t = Trajectoire(150.00, 350.00, 210.00, 70.00)
        t = Trajectoire(210.00, 70.00, 150.00, 350.00)
        liste = t.getListe()
        self.__AfficherTrajectoire(liste)

if __name__ == '__main__':
    app = wx.App()
    Example(None, 'Line')
    app.MainLoop()


