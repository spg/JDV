#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx


class Obstacle(wx.Frame):
    def __init__( self,parent, title):
        wx.Frame.__init__(self, parent=parent , title=title, size=(300,300))
        self.initUi()
        self.bindHandlers()


    def initUi(self):
        panel1 = wx.Panel(self, -1)

        self.label1 = wx.StaticText(panel1, -1, 'x1 :' ,pos=(30, 50))
        self.label1 = wx.StaticText(panel1, -1, 'y1 :' ,pos=(130, 50))
        self.label1 = wx.StaticText(panel1, -1, 'x2 :' ,pos=(30, 150))
        self.label1 = wx.StaticText(panel1, -1, 'y2 :' ,pos=(130, 150))
        self.x1 = wx.TextCtrl(panel1,-1,value=u"",pos=(50, 50),size=(50,20))
        self.y1 = wx.TextCtrl(panel1,-1,value=u"",pos=(150, 50),size=(50,20))
        self.x2 = wx.TextCtrl(panel1,-1,value=u"",pos=(50, 150),size=(50,20))
        self.y2 = wx.TextCtrl(panel1,-1,value=u"",pos=(150, 150),size=(50,20))
        self.ajoute = wx.Button(panel1, label="Ajouter", pos=(50, 200),size=(75,20))
        self.annule = wx.Button(panel1, label="Annuler", pos=(150, 200),size=(75,20))




    def bindHandlers(self):
        self.Bind(wx.EVT_BUTTON, self.onAjouteClicked, self.ajoute)

    def onAjouteClicked(self):
        self.dx1 = self.x1.GetValue()
        self.dx2 = self.x2.GetValue()
        self.dy1 = self.y1.GetValue()
        self.dy2 = self.y2.GetValue()
        self.Show(False)

    def getx1(self):
        return int(self.dx1)

    def getx2(self):
        return int(self.dx2)

    def gety1(self):
        return int(self.dy1)

    def gety2(self):
        return int(self.dy2)


