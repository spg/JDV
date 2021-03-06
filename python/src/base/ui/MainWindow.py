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
from python.src.base.endevent import EndEvent
from python.src.base.confirmevent import ConfirmEvent

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent, title=title,
            size=(900, 550))
        self.panel = wx.Panel(self, -1)
        self.__Action = True
        self.Tour =1
        self.__Obstacle = False
        self.Dessin = False
        self.Chemin = False
        self.gap = 20
        self.t1= 0
        self.__robotx = 175*2
        self.__roboty = 53*2
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
        EndEvent.addHandler(self.__endReceived)
        ConfirmEvent.addHandler(self.__ConfirmReceived)

    def __bindHandlers(self):
        self.Bind(wx.EVT_BUTTON, self.__onNewturnButtonClicked, self.__startnew)
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
        self.dc.DrawRectangle(156+ self.__offset, 0 + self.__offset, 4,220 )
        # Point d'arriver pour les dessins
        self.dc.SetBrush(wx.Brush('#00ff00'))
        #self.dc.DrawRectangle( 122+ self.__offset, 182 + self.__offset, 5, 5)
        #self.dc.DrawRectangle( 46+ self.__offset, 182 + self.__offset, 5, 5)
        #self.dc.DrawRectangle( 40+ self.__offset, 190 + self.__offset, 5, 5)
        #self.dc.DrawRectangle( 40+ self.__offset, 138 + self.__offset, 5, 5)
        #self.dc.DrawRectangle( 40+ self.__offset, 84 + self.__offset, 5, 5)
        #self.dc.DrawRectangle( 40+ self.__offset, 32 + self.__offset, 5, 5)
        #self.dc.DrawRectangle( 46+ self.__offset, 40 + self.__offset, 5, 5)
        #self.dc.DrawRectangle( 122+ self.__offset, 40 + self.__offset, 5, 5)
        # Point d'arriver pour la zone de  dessins
        #self.dc.DrawRectangle( 295 + self.__offset, 55 + self.__offset, 5, 5)
        # Met le robot sur la zone
        self.dc.SetBrush(wx.Brush('#ff0000'))
        self.__xL1 = self.__robotx + (15 * self.__coordx1)
        self.__xL2 = self.__robotx + (15 * self.__coordx2)
        self.__yL1 = self.__roboty + (15 * self.__coordy1)
        self.__yL2 = self.__roboty + (15 * self.__coordy2)
        self.dc.DrawLine(self.__robotx, self.__roboty, self.__xL1, self.__yL1)
        self.dc.DrawLine(self.__robotx, self.__roboty, self.__xL2, self.__yL2)
        self.dc.DrawLine(self.__xL2, self.__yL2, self.__xL1, self.__yL1)
        if self.__Obstacle:
            self.dc.SetBrush(wx.Brush('#0000ff'))
            self.dc.DrawRectangle(self.__x1*2, (100-self.__y1)*2, 20, 20)
            #self.dc.DrawRectangle(self.__x1*2, (self.__y1)*2, 20, 20)
            self.dc.SetBrush(wx.Brush('#ff0000'))
            self.dc.DrawRectangle(self.__x2*2, (100-self.__y2)*2, 20, 20)
            #self.dc.DrawRectangle(self.__x2*2, (self.__y2)*2, 20, 20)
            gap = self.gap
            gap2 = gap +10

            self.x21=gap2+self.__x2
            self.x22=gap2+self.__x2
            self.x23=self.__x2-gap
            self.x24=self.__x2-gap
            self.y21=self.__y2-gap
            self.y22=gap2+self.__y2
            self.y23=self.__y2-gap
            self.y24=gap2+self.__y2
            self.x11=gap2+self.__x1
            self.x12=gap2+self.__x1
            self.x13=self.__x1-gap
            self.x14=self.__x1-gap
            self.y11=gap2+self.__y1
            self.y12=self.__y1-gap
            self.y13=gap2+self.__y1
            self.y14=self.__y1-gap
            #self.dc.SetBrush(wx.Brush('#ff0000'))
            #self.dc.DrawRectangle(self.x21*2,self.y21*2, 5, 5)
            #self.dc.DrawRectangle(self.x22*2,self.y22*2, 5, 5)
            #self.dc.DrawRectangle(self.x23*2,self.y23*2, 5, 5)
            #self.dc.DrawRectangle(self.x24*2,self.y24*2, 5, 5)
            #self.dc.SetBrush(wx.Brush('#0000ff'))
            #self.dc.DrawRectangle(self.x11*2, self.y11*2, 5, 5)
            #self.dc.DrawRectangle(self.x12*2, self.y12*2, 5, 5)
            #self.dc.DrawRectangle(self.x13*2, self.y13*2, 5, 5)
            #self.dc.DrawRectangle(self.x14*2, self.y14*2, 5, 5)

        if self.__Action:
            self.__Action = False
            self.__button = wx.Button(self.panel, label="Obstacle", pos=(500, 10), size=(100, 25))
            self.__Affiche = wx.Button(self.panel, label="Affiche", pos=(500, 50), size=(100, 25))
            self.__connectionButton = wx.Button(self.panel, label="Se connecter au ", pos=(500, 90), size=(130, 25))
            self.__startnew = wx.Button(self.panel, label="Nouveau tour", pos=(500, 140), size=(130, 25))
            self.__loggingArea = wx.TextCtrl(self.panel, pos=(270, 260), size=(200, 200), style=wx.TE_MULTILINE)
            self.__ipTextCtrl = wx.TextCtrl(self.panel, value='10.240.254.168', pos=(500, 200), size=(100, 25))
            self.__portTextCtrl = wx.TextCtrl(self.panel, value='', pos=(650, 200), size=(100, 25))
            self.__Info = wx.TextCtrl(self.panel, value='', pos=(500, 240), size=(300, 100))
            font1 = wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Comic Sans MS')
            self.__TimeInfo = wx.TextCtrl(self.panel, value='', pos=(500, 340), size=(300, 300),style=wx.TE_MULTILINE)
            self.__TimeInfo.SetForegroundColour((0,0,255))
            self.__TimeInfo.SetFont(font1)
            self.__Info.SetForegroundColour((0,255,0))
            self.__Info.SetFont(font1)
            self.__Info.AppendText("")
            self.label1 = wx.StaticText(self.panel, -1, 'x1 :' ,pos=(670, 50))
            self.label2 = wx.StaticText(self.panel, -1, 'y1 :' ,pos=(770, 50))
            self.label3 = wx.StaticText(self.panel, -1, 'x2 :' ,pos=(670, 150))
            self.label4 = wx.StaticText(self.panel, -1, 'y2 :' ,pos=(770, 150))
            self.x1 = wx.TextCtrl(self.panel,-1,value=u"111",pos=(700, 50),size=(50,20))
            self.y1 = wx.TextCtrl(self.panel,-1,value=u"48",pos=(800, 50),size=(50,20))
            self.x2 = wx.TextCtrl(self.panel,-1,value=u"100",pos=(700, 150),size=(50,20))
            self.y2 = wx.TextCtrl(self.panel,-1,value=u"82",pos=(800, 150),size=(50,20))
            # mac mini 254.168  10.240.213.142
            self.__bindHandlers()

    def __onNewturnButtonClicked(self, event):
        self.t1 = time.clock()
        print ""
        self.__base.NewTurn()

    def __onConnectButtonClicked(self, event):
        #Affiche les obstacle
        self.__x1=int(self.x1.GetValue())
        self.__x2=int(self.x2.GetValue())
        self.__y1=int(self.y1.GetValue())
        self.__y2=int(self.y2.GetValue())
        #Affichage des obstacle
        self.__Obstacle= True
        self.dc.Clear()
        self.__DrawLine()
        self.t1 = time.clock()
        self.__connectionButton.Disable()
        self.__ipTextCtrl.Disable()
        self.__base.connectToRobot(self.__ipTextCtrl.GetValue(),self.__portTextCtrl.GetValue())
        self.__base.setObstacle(self.__x1, self.__y1, self.__x2, self.__y2)
        self.__base.StartRobot()

    def __ConfirmReceived(self, message):
        wx.CallAfter(self.__printToLoggingInfo, message)

    def __endReceived(self,message):
        t2 = time.clock()
        total = t2 - self.t1
        min = int(round(total/60,0))
        sec = int(round(total%60,0))

        if min < 10 > sec:
            message = "temps :  0" + str(min) + ":0" + str(sec)
        if min < 10 <= sec:
            message = "temps :  0" + str(min) + ":" + str(sec)
        if min >= 10 > sec:
            message = "temps :  " + str(min) + ":0" + str(sec)
        if min >= 10 <= sec:
            message = "temps :  " + str(min) + ":" + str(sec)


        wx.CallAfter(self.__printTemps, message)

    def __logReceived(self, message):
        wx.CallAfter(self.__printToLoggingArea, message)

    def __PoseReceived(self, message):
        wx.CallAfter(self.__Pose,message)

    def __Pose(self,message):
        self.dc.Clear()
        Angle = message.theta
        self.__RotationTriangle(Angle)
        self.__robotx = message.x*2
        self.__roboty = (110-message.y)*2
        #self.__roboty = (message.y)*2
        self.__DrawLine()
        if self.Dessin:
            self.__AfficherDessin(self.__listeDessin)
        if self.Chemin:
            self.__AfficherTrajectoire(self.__listeChemin)

    def __DessinReceived(self, message):
        wx.CallAfter(self.__Dessin,message)


    def __Dessin(self,message):
        self.Dessin =True
        self.__listeDessin= message.liste
        self.__AfficherDessin(self.__listeDessin)

    def __TrajectoireReceived(self, message):
        wx.CallAfter(self.__trajectoire,message)

    def __trajectoire(self,message):
        self.Chemin =True
        self.__listeChemin = message.liste
        self.__AfficherTrajectoire(self.__listeChemin)

    def __AfficherTrajectoire(self, liste):
        self.dc.Clear()
        self.__DrawLine()
        if self.Dessin:
            self.__AfficherDessin(self.__listeDessin)
        Depart = True
        x1  = y1 = 0
        for  x, y  in liste :
            if Depart :
                Depart = False
            else:
                #self.dc.DrawLine((x1*2)+self.__offset,(y1*2)+self.__offset, (x*2)+self.__offset,(y*2)+self.__offset)
                self.dc.DrawLine((x1*2)+self.__offset,((110-y1)*2)+self.__offset, (x*2)+self.__offset,((110-y)*2)+self.__offset)
            x1 = x
            y1 = y



    def __AfficherDessin(self,liste):
        self.Dessin = True
        self.dc.Clear()
        print "Efface"
        self.__DrawLine()
        Depart = True
        x1 = y1 = 0
        for  x, y  in liste :
            print "DEssin"
            if Depart :
                xdepart = x
                ydepart = y
                Depart = False
            else:
                self.dc.DrawLine((x1*4)+self.__offset, (-y1*4)+ 470, (x*4)+self.__offset, (-y*4)+470)
            x1 = x
            y1 = y
        self.dc.DrawLine((x*4)+self.__offset, (-y*4)+ 470, (xdepart*4)+self.__offset, (-ydepart*4)+470)

    def __printToLoggingArea(self, message):
        currentTime = time.strftime("%H:%M:%S", time.localtime())
        self.__loggingArea.AppendText(currentTime + ' : ' + message + '\n')


    def __printTemps(self, message):
        self.__TimeInfo.AppendText('Tour '+str(self.Tour)+' : ')
        print str(message)
        self.__TimeInfo.AppendText(message+'\n')
        self.Tour += 1

    def __printToLoggingInfo(self, message):
        print str(message)
        self.__Info.SetValue(message)

    def __RotationTriangle(self, angles):
        x = ((self.__robotx - self.__xL1 ) / 15)
        y = ((self.__roboty - self.__yL1) / 15)
        _angle = angles - self.__angleActuelle
        self.__angleActuelle += _angle
        self.__coordx1 = 0 - (x * math.cos(math.radians(_angle)) - (y * math.sin(math.radians(_angle))))
        self.__coordy1 = 0 - (x * math.sin(math.radians(_angle)) + (y * math.cos(math.radians(_angle))))
        x1 = ((self.__robotx - self.__xL2) / 15)
        y1 = ((self.__roboty - self.__yL2) / 15)
        self.__coordx2 = 0 - (x1 * math.cos(math.radians(_angle)) - (y1 * math.sin(math.radians(_angle))))
        self.__coordy2 = 0 - (x1 * math.sin(math.radians(_angle)) + (y1 * math.cos(math.radians(_angle))))

    def __onButtonClicked(self, event):
        O = Obstacle(None,"Obstacle")
        O.Show()

    def __onAfficheClicked(self, event):
        #Affiche les obstacle
        self.__x1=int(self.x1.GetValue())
        self.__x2=int(self.x2.GetValue())
        self.__y1=int(self.y1.GetValue())
        self.__y2=int(self.y2.GetValue())
        #Valeur par default pour bu de test
        #self.__x1 =  120+ self.__offset
        #self.__y1 =  50+self.__offset
        #self.__x2 =  110+ self.__offset
        #self.__y2 =  50+self.__offset
        #self.__x2 =  50+ self.__offset
        #self.__y2 =  100+self.__offset
        #self.__x1 =  80+ self.__offset
        #self.__y1 =  50+self.__offset
        #Affichage des obstacle
        # Bleu
        self.dc.SetBrush(wx.Brush('#0000ff'))
        self.dc.DrawRectangle(self.__x1*2, self.__y1*2, 20, 20)
        # Rouge
        self.dc.SetBrush(wx.Brush('#ff0000'))
        self.dc.DrawRectangle(self.__x2*2, self.__y2*2, 20, 20)
        self.__Obstacle= True
        #Affichage des noeuds des obstacles
        #t = Trajectoire(150.00, 350.00, 210.00, 70.00)
        t = Trajectoire(self.__x1,self.__y1 ,self.__x2 ,self.__y2)
        #liste = t.PathFinding(175.00, 60.00,25.00, 105.00 )
        #self.__AfficherTrajectoire(liste)
        liste =t.PathFinding(56.0, 50.0, 175.00, 53.00 )
        self.__AfficherTrajectoire(liste)
        time.sleep(2)
        liste =t.PathFinding(30.0, 40.0, 175.00, 53.00 )
        self.__AfficherTrajectoire(liste)
        time.sleep(2)
        liste =t.PathFinding(50.0, 16.0, 175.00, 53.00 )
        self.__AfficherTrajectoire(liste)
        time.sleep(2)
        liste =t.PathFinding(56.0, 60.0, 175.00, 53.00 )
        self.__AfficherTrajectoire(liste)
        time.sleep(2)
        liste =t.PathFinding(40.0, 42.0, 175.00, 53.00 )
        self.__AfficherTrajectoire(liste)
        time.sleep(2)
        liste =t.PathFinding(40.0, 69.0, 175.00, 53.00 )
        self.__AfficherTrajectoire(liste)
        time.sleep(2)
        liste =t.PathFinding(40, 77, 175.00, 53.00 )
        self.__AfficherTrajectoire(liste)
        time.sleep(2)
        liste =t.PathFinding(30.0, 71.0, 175.00, 53.00 )
        self.__AfficherTrajectoire(liste)
        time.sleep(2)
        liste =t.PathFinding(56.0, 60.0, 175.00, 53.00 )
        self.__AfficherTrajectoire(liste)


