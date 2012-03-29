#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

author: Equipe 5
"""
import math
import time
import wx
import networkx as nx
from python.src.base.ui.Trajectoire import  Trajectoire
from python.src.base.Base import Base
from python.src.base.logevent import LogEvent
from python.src.base.poseevent import PoseEvent
from python.src.base.trajectoireevent import TrajectoireEvent
from python.src.base.dessinevent import DessinEvent
from python.src.base.ui.Obstacle import  Obstacle


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent, title=title,
            size=(700, 550))
        self.panel = wx.Panel(self, -1)
        self.__Action = True
        self.__robotx = 60
        self.__roboty = 60
        self.__angleActuelle = 0
        self.__coordx1 = -1
        self.__coordy1 = -1
        self.__coordx2 = -1
        self.__coordy2 = 1
        self.__base = Base()
        wx.FutureCall(2000, self.__DrawLine)
        self.Centre()
        self.Show()
        LogEvent.addHandler(self.__logReceived)
        PoseEvent.addHandler(self.__PoseReceived)
        TrajectoireEvent.addHandler(self.__TrajectoireReceived)
        DessinEvent.addHandler(self.__DessinReceived)


    def __bindHandlers(self):
        self.Bind(wx.EVT_BUTTON, self.__onButtonClicked, self.__button)
        self.Bind(wx.EVT_BUTTON, self.__onAfficheClicked, self.__Affiche)
        self.Bind(wx.EVT_BUTTON, self.__onConnectButtonClicked, self.__connectionButton)


    def __DrawLine(self):
        #option de décalage


        self.__offset = 0
        self.dc = wx.ClientDC(self.panel)
        # La zone de jeux
        self.dc.SetBrush(wx.Brush('#ffffff'))
        self.dc.DrawRectangle(0 + self.__offset, 0 + self.__offset, 460, 220)
        self.dc.DrawRectangle(0 + self.__offset, 230 + self.__offset, 240, 240)
        # Aire de dessin
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle(284+ self.__offset,44  + self.__offset, 133, 133)
        self.dc.SetBrush(wx.Brush('#ffffff'))
        self.dc.DrawRectangle(290 + self.__offset, 50 + self.__offset, 121, 121)
        #ligne rouge
        self.dc.SetBrush(wx.Brush('#ff0000'))
        self.dc.DrawRectangle(158 + self.__offset, 0 + self.__offset, 4,220 )
        # Point d'arriver pour les dessins
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle( 122+ self.__offset, 182 + self.__offset, 5, 5)
        self.dc.DrawRectangle( 46+ self.__offset, 182 + self.__offset, 5, 5)
        self.dc.DrawRectangle( 40+ self.__offset, 190 + self.__offset, 5, 5)
        self.dc.DrawRectangle( 40+ self.__offset, 138 + self.__offset, 5, 5)
        self.dc.DrawRectangle( 40+ self.__offset, 84 + self.__offset, 5, 5)
        self.dc.DrawRectangle( 40+ self.__offset, 32 + self.__offset, 5, 5)
        self.dc.DrawRectangle( 46+ self.__offset, 40 + self.__offset, 5, 5)
        self.dc.DrawRectangle( 122+ self.__offset, 40 + self.__offset, 5, 5)
        # Point d'arriver pour la zone de  dessins
        self.dc.DrawRectangle( 295 + self.__offset, 55 + self.__offset, 5, 5)
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
            self.__loggingArea = wx.TextCtrl(self.panel, pos=(270, 260), size=(200, 200), style=wx.TE_MULTILINE)
            self.__ipTextCtrl = wx.TextCtrl(self.panel, value='10.240.247.59', pos=(500, 140), size=(100, 25))
            self.__bindHandlers()

    def __onConnectButtonClicked(self, event):
        #Affiche les obstacle
        # __x1=self.O.getx1()+self.__offset
        #__x2=self.O.getx2()+self.__offset
        #__y1=self.O.gety1()+self.__offset
        #__y1=self.O.gety2()+self.__offset
        __x1 = 90+ self.__offset
        __y1 = 70+ self.__offset
        __x2 = 0+ self.__offset
        __y2 = 0+ self.__offset
        #Affichage des obstacle
        self.dc.SetBrush(wx.Brush('#0000ff'))
        self.dc.DrawRectangle(__x1*2, abs(__y1-110)*2, 20, 20)
        self.dc.SetBrush(wx.Brush('#ff0000'))
        self.dc.DrawRectangle(__x2*2, abs(__y2-110)*2, 20, 20)
        self.__connectionButton.Disable()
        self.__ipTextCtrl.Disable()
        self.__base.connectToRobot(self.__ipTextCtrl.GetValue())
        self.__base.setObstacle(__x1, __y1, __x2, __y2)
        self.__base.StartRobot()


    def __logReceived(self, message):
        wx.CallAfter(self.__printToLoggingArea, message)

    def __PoseReceived(self, message):
        self.dc.Clear()
        Angle = message.theta
        self.__RotationTriangle(Angle)
        self.__robotx = message.x
        self.__roboty = message.y
        self.__DrawLine()

    def __DessinReceived(self, message):
        self.__AfficherDessin(message.liste)


    def __TrajectoireReceived(self, message):
        self.__AfficherTrajectoire(message.liste)

    def __AfficherTrajectoire(self, liste):
        Depart = True
        x1  = y1 = 0
        for  x, y  in liste :
            if Depart :
                Depart = False
            else:
                self.dc.DrawLine((x1*2)+self.__offset,((110-y1)*2)+self.__offset, (x*2)+self.__offset,((110-y)*2)+self.__offset)
            x1 = x
            y1 = y



    def __AfficherDessin(self,liste):
        Depart = True
        x1 = y1 = 0
        for  x, y  in liste :
            if Depart :
                Depart = False
            else:
                self.dc.DrawLine((x1*4)+self.__offset, (-y1*4)+ 470, (x*4)+self.__offset, (-y*4)+470)
            x1 = x
            y1 = y

    def __printToLoggingArea(self, message):
        currentTime = time.strftime("%H:%M:%S", time.localtime())
        self.__loggingArea.AppendText(currentTime + ' : ' + message + '\n')

    def __RotationTriangle(self, angles):
        x = ((self.__robotx - self.__xL1 ) / 10)
        y = ((self.__roboty - self.__yL1) / 10)
        _angle = angles - self.__angleActuelle
        self.__angleActuelle += _angle
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
        self.__x1 = 90+ self.__offset
        self.__y1 = 70+ self.__offset
        self.__x2 = 0+ self.__offset
        self.__y2 = 0+ self.__offset
        #Affichage des obstacle
        self.dc.SetBrush(wx.Brush('#0000ff'))
        self.dc.DrawRectangle(self.__x1*2, (110-self.__y1)*2, 20, 20)
        self.dc.SetBrush(wx.Brush('#ff0000'))
        self.dc.DrawRectangle(self.__x2*2, (110-self.__y2)*2, 20, 20)
        #Affichage des noeuds des obstacles
        #t = Trajectoire(150.00, 350.00, 210.00, 70.00)
        t = Trajectoire(self.__x1,self.__y1 ,self.__x2 ,self.__y2)
        liste = t.PathFinding(207.00, 22.50,20.00, 95.00 )
        self.__AfficherTrajectoire(liste)
        #liste = t.PathFinding(207.8, 88.5, 174.8 , 55.5)
        #self.__AfficherTrajectoire(liste)
        #liste = t.PathFinding(174.8, 55.5, 23 , 91)
        #self.__AfficherTrajectoire(liste)



