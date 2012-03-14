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
import networkx as nx
from src.base.ui.Obstacle import  Obstacle





class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(1000, 1000))
        self.panel = wx.Panel(self, -1)
        self.countAction = 0
        self.Action=True
        self.robotx = 50
        self.angleActuelle=0
        self.roboty = 50
        self.coordx1 = -1
        self.coordy1 = -1
        self.coordx2 = 1
        self.coordy2 = -1
        self.__base = Base()
        self.i = 0
        wx.FutureCall(2000, self.DrawLine)
        self.direction=1
        self.gr = nx.Graph()
        self.Centre()
        self.Show()
        LogEvent.addHandler(self.__logReceived)


    def bindHandlers(self):
        self.Bind(wx.EVT_BUTTON, self.onButtonClicked, self.button)
        self.Bind(wx.EVT_BUTTON, self.onAfficheClicked, self.Affiche)
        self.Bind(wx.EVT_BUTTON, self.__onConnectButtonClicked, self.__connectionButton)





    def DrawLine(self):
        #option de décalage

        self.d  = 10
        self.dc = wx.ClientDC(self.panel)

        # La zone de jeux
        self.dc.SetBrush(wx.Brush('#ffffff'))
        self.dc.DrawRectangle(0+self.d, 0+self.d, 220, 460)
        # Aire de dessin
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle(44+self.d, 228+self.d, 133, 133)
        self.dc.SetBrush(wx.Brush('#ffffff'))
        self.dc.DrawRectangle(50+self.d, 234+self.d, 121, 121)
        #ligne rouge
        self.dc.SetBrush(wx.Brush('#ff0000'))
        self.dc.DrawRectangle(0+self.d, 158+self.d, 220, 4)
        # Point d'arriver pour les dessins
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle(20+self.d, 10+self.d, 5, 5)
        self.dc.DrawRectangle(70+self.d, 10+self.d, 5, 5)
        self.dc.DrawRectangle(130+self.d, 10+self.d, 5, 5)
        self.dc.DrawRectangle(190+self.d, 10+self.d, 5, 5)
        self.dc.DrawRectangle(20+self.d, 30+self.d, 5, 5)
        self.dc.DrawRectangle(20+self.d, 60+self.d, 5, 5)
        self.dc.DrawRectangle(190+self.d, 30+self.d, 5, 5)
        self.dc.DrawRectangle(190+self.d, 60+self.d, 5, 5)
        # Point d'arriver pour la zone de  dessins
        self.dc.DrawRectangle(55+self.d, 240+self.d, 5, 5)
        # Met le robot sur la zone
        self.dc.SetBrush(wx.Brush('#ff0000'))
        self.xL1=self.robotx+(10*self.coordx1)
        self.xL2=self.robotx+(10*self.coordx2)
        self.yL1=self.roboty+(10*self.coordy1)
        self.yL2=self.roboty+(10*self.coordy2)
        print "robotx:%d" % self.robotx
        print "roboty:%d" % self.roboty
        print "xL1 :%d" % self.xL1
        print "yL1 :%d" % self.yL1
        print "xL2 :%d" % self.xL2
        print "yL2 :%d" % self.yL2
        self.dc.DrawLine(self.robotx,self.roboty,self.xL1,self.yL1)
        self.dc.DrawLine(self.robotx,self.roboty,self.xL2,self.yL2)
        self.dc.DrawLine(self.xL2,self.yL2,self.xL1,self.yL1)
        if self.Action==True:
            self.Action=False
            self.button = wx.Button(self.panel, label="Obstacle", pos=(50, 500),size=(100,25))
            self.Affiche = wx.Button(self.panel, label="Affiche", pos=(50, 550),size=(100,25))
            self.__connectionButton = wx.Button(self.panel, label="Se connecter au: ", pos=(50, 600), size=(130, 25))
            self.__loggingArea = wx.TextCtrl(self.panel, pos=(350,500), size=(200,200), style=wx.TE_MULTILINE)
            self.__ipTextCtrl = wx.TextCtrl(self.panel, value='10.240.254.168', pos=(200, 600), size=(100, 25))
            self.bindHandlers()

    def __onConnectButtonClicked(self, event):
        self.__connectionButton.Disable()
        self.__ipTextCtrl.Disable()
        self.__base.connectToRobot(self.__ipTextCtrl.GetValue())

    def __logReceived(self, message):

        if self.countAction==0:
            wx.CallAfter(self.__printToLoggingArea, message)
            self.mes = message
            self.countAction = self.countAction+1
        elif self.countAction == 1:
            if self.mes =="Received pose:" :
                self.dc.Clear()
                Angle= message.theta
                self.RotationTriangle(Angle)
                self.robotx = message.x
                self.roboty = message.y
                self.countAction = -1
                self.DrawLine()
                self.countAction =0
            elif self.mes =="Received Line:" :
                self.dc.DrawLine(message.x1,message.y1,message.x2,message.y2)

    def __printToLoggingArea(self, message):
        currentTime = time.strftime("%H:%M:%S", time.localtime())
        self.__loggingArea.AppendText(currentTime + ' : ' + message +'\n')

    def RotationTriangle(self,angle):
        x = ((self.robotx-self.xL1 )/ 10)
        y = ((self.roboty-self.yL1)/10)
        print "x :%d" % x
        print "y :%d" % y
        _angle = angle - self.angleActuelle
        self.angleActuelle = self.angleActuelle + _angle
        print "_angle :%d" % _angle
        print "angleActuelle :%d" % self.angleActuelle
        self.coordx1 = 0-(x*math.cos(math.radians(_angle)) - (y*math.sin(math.radians(_angle))))
        self.coordy1 = 0-(x*math.sin(math.radians(_angle)) + (y*math.cos(math.radians(_angle))))
        #print "coordy :%d" % self.coordy1
        #print "coordx :%d" % self.coordx1
        x1 = ((self.robotx- self.xL2)/ 10)
        y1 = ((self.roboty-self.yL2)/10)
        #print "x2 :%d" % x1
        #print "y2 :%d" % y1
        self.coordx2 = 0-(x1*math.cos(math.radians(_angle)) - (y1*math.sin(math.radians(_angle))))
        self.coordy2 = 0-(x1*math.sin(math.radians(_angle)) + (y1*math.cos(math.radians(_angle))))

    def onButtonClicked(self):
        O = Obstacle()
        O.Show()

    def onAfficheClicked(self):

        #Affiche les obstacle
        #self.x1=self.O.getx1()+self.d
        #self.x2=self.O.getx2()+self.d
        #self.y1=self.O.gety1()+self.d
        #self.y2=self.O.gety2()+self.d
        #Valeur par default pour bu de test
        self.x1=140+self.d
        self.y1=250+self.d
        self.x2=140+self.d
        self.y2=150+self.d



        #Affichage des obstacle
        self.dc.SetBrush(wx.Brush('#000000'))
        self.dc.DrawRectangle(self.x1, self.y1, 20, 20)
        self.dc.DrawRectangle(self.x2, self.y2, 20, 20)
        #Affichage des noeuds des obstacles

        t = Trajectoire(150.00,350.00,210.00,70.00)

if __name__ == '__main__':
    app = wx.App()
    Example(None, 'Line')
    app.MainLoop()


