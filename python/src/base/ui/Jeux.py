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
import threading
import wx
import networkx as nx




class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(1000, 1000))
        self.panel = wx.Panel(self, -1)
        self.Action=True
        self.robotx = 50
        self.roboty = 50
        self.i = 0
        wx.FutureCall(2000, self.DrawLine)
        self.direction=1
        self.gr = nx.Graph()
        self.Centre()
        self.Show()



    def bindHandlers(self):
        self.Bind(wx.EVT_BUTTON, self.onButtonClicked, self.button)
        self.Bind(wx.EVT_BUTTON, self.onAfficheClicked, self.Affiche)

    def CreerGraph(self):
        #Initialise les noueds
        self.gr.add_node("Depart")
        self.gr.add_node("Fin")
        self.gr.add_node("O11")
        self.gr.add_node("O12")
        self.gr.add_node("O13")
        self.gr.add_node("O14")
        self.gr.add_node("O21")
        self.gr.add_node("O22")
        self.gr.add_node("O23")
        self.gr.add_node("O24")
        #Initialisation des arcs



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
        self.dc.DrawRectangle(self.robotx,self.roboty,10,10)
        if self.direction==1:
            self.dc.DrawRectangle(self.robotx-5,self.roboty+10,20,5)
            self.dc.DrawRectangle(self.robotx-2.5,self.roboty+15,15,5)
            self.dc.DrawRectangle(self.robotx,self.roboty+20,10,5)
        if self.direction==2:
            self.dc.DrawRectangle(self.robotx+10,self.roboty+-5,5,20)
            self.dc.DrawRectangle(self.robotx+15,self.roboty-2.5,5,15)
            self.dc.DrawRectangle(self.robotx+20,self.roboty,5,10)
        if self.direction==3:
            self.dc.DrawRectangle(self.robotx-5,self.roboty-5,20,5)
            self.dc.DrawRectangle(self.robotx-2.5,self.roboty-10,15,5)
            self.dc.DrawRectangle(self.robotx,self.roboty-15,10,5)
        if self.direction==4:
            self.dc.DrawRectangle(self.robotx-5,self.roboty-5,5,20)
            self.dc.DrawRectangle(self.robotx-10,self.roboty-2.5,5,15)
            self.dc.DrawRectangle(self.robotx-15,self.roboty,5,10)
        if self.Action==True:
            self.Action=False
            self.button = wx.Button(self.panel, label="Obstacle", pos=(500, 500),size=(100,50))
            self.Affiche = wx.Button(self.panel, label="Affiche", pos=(700, 500),size=(100,50))
            self.bindHandlers()

    def onButtonClicked(self, event):
        self.__fetchCurrentPose()

    def onAfficheClicked(self, event):

        #Affiche les obstacle
        #self.x1=self.O.getx1()+self.d
        #self.x2=self.O.getx2()+self.d
        #self.y1=self.O.gety1()+self.d
        #self.y2=self.O.gety2()+self.d
        #Valeur par default pour bu de test
        self.x1=130+self.d
        self.y1=250+self.d

        self.Ox11=35+self.x1
        self.Ox12=35+self.x1
        self.Ox13=self.x1-20
        self.Ox14=self.x1-20
        self.Oy11=35+self.y1
        self.Oy12=self.y1-20
        self.Oy13=35+self.y1
        self.Oy14=self.y1-20

        self.x2=200+self.d
        self.y2=150+self.d

        self.Ox21=35+self.x2
        self.Ox22=35+self.x2
        self.Ox23=self.x2-20
        self.Ox24=self.x2-20
        self.Oy21=35+self.y2
        self.Oy22=self.y2-20
        self.Oy23=35+self.y2
        self.Oy24=self.y2-20

        #Affichage des obstacle
        self.dc.SetBrush(wx.Brush('#000000'))
        self.dc.DrawRectangle(self.x1, self.y1, 20, 20)
        self.dc.DrawRectangle(self.x2, self.y2, 20, 20)
        #Affichage des noeuds des obstacle 1
        self.dc.SetBrush(wx.Brush('#0000ff'))
        self.dc.DrawRectangle(self.Ox21,self.Oy21, 5, 5)
        self.dc.DrawRectangle(self.Ox22,self.Oy22, 5, 5)
        self.dc.DrawRectangle(self.Ox23,self.Oy23, 5, 5)
        self.dc.DrawRectangle(self.Ox24,self.Oy24, 5, 5)
        #Affichage des noeuds des obstacle 1
        self.dc.DrawRectangle(self.Ox11,self.Oy11, 5, 5)
        self.dc.DrawRectangle(self.Ox12,self.Oy12, 5, 5)
        self.dc.DrawRectangle(self.Ox13,self.Oy13, 5, 5)
        self.dc.DrawRectangle(self.Ox14,self.Oy14, 5, 5)
        #Ajout des noueds des obstacle
        #Ajout des chemein possible
        self.Trouvetrajectoire(210.00,350.00,210.00,70.00)
        grs = nx.Graph()
        grs = nx.shortest_path(self.gr,"Depart","Fin")
        print grs



    def Trouvetrajectoire(self,Posdx,Posdy,Posfx,Posfy):
        self.TrouveO = True
        self.TrouveO1 = False
        self.TrouveO2 = False
        self.ParcourireLigne(Posdx,Posdy,Posfx,Posfy,"Depart")
        while(self.TrouveO == True):
            self.TrouveO=False
            if self.TrouveO1==True:
                self.TrouveO1=False
                self.ParcourireLigne(self.Ox12,self.Oy12,Posfx,Posfy,"O12")
                self.ParcourireLigne(self.Ox14,self.Oy14,Posfx,Posfy,"O14")
            if self.TrouveO2==True:
                self.TrouveO2=False
                self.ParcourireLigne(self.Ox22,self.Oy22,Posfx,Posfy,"O22")
                self.ParcourireLigne(self.Ox24,self.Oy24,Posfx,Posfy,"O24")


    def ParcourireLigne(self,Posdx,Posdy,Posfx,Posfy,depart):
        ad = abs(Posdx-Posfx)
        bd = abs(Posdy-Posfy)
        tanA = ad/bd


        #self.dc.DrawLine(Posdx,Posdy, Posfx, Posfy)
        b =1

        self.TrouveO = False
        while bd > b and self.TrouveO ==False :
            a = (tanA * b)
            posx = a + Posdx
            #print "a :%d" % a
            #print "b :%d" % b
            #print "posx :%d" % posx
            posy = Posdy - b
            #print "posy :%d" % posy
            if posy>= self.Oy24 and posy<=self.Oy21  and posx>=self.Ox24 and posx<=self.Ox21:
                # Calcule des distances
                disty=self.Oy21 - Posdy
                self.verifierTrajectoire(Posdx,Posdy,self.Ox21,self.Oy21)
                if self.Ox21 < 220  and self.Ox21 >0 and self.TrouveVO == False :
                    distx= self.Ox21 - Posdx
                    c = distx**2 + disty**2
                    dist = math.sqrt(c)

                    self.dc.DrawLine(Posdx, Posdy, self.Ox21, self.Oy21)
                    self.gr.add_edge(depart,"O21" , weight=dist )
                    self.gr.add_edge("O21","O22" , weight=5 )
                    self.dc.DrawLine(self.Ox21, self.Oy21, self.Ox22, self.Oy22)
                self.verifierTrajectoire(Posdx,Posdy,self.Ox23,self.Oy23)
                if self.Ox23 < 220  and self.Ox23 > 0 and self.TrouveVO == False :
                    distx= self.Ox23 - Posdx
                    c = distx**2 + disty**2
                    dist = math.sqrt(c)
                    self.dc.DrawLine(Posdx, Posdy, self.Ox23, self.Oy23)
                    self.gr.add_edge(depart,"O23" , weight=dist )
                    self.gr.add_edge("O23","O24" , weight=5 )
                    self.dc.DrawLine(self.Ox23, self.Oy23, self.Ox24, self.Oy24)
                self.TrouveO = True
                self.TrouveO2=True

            if posy >= self.Oy14 and posy<=self.Oy11  and posx>=self.Ox14 and posx<=self.Ox11:
                self.verifierTrajectoire(Posdx,Posdy,self.Ox11,self.Oy11)
                # Calcule des distances
                disty=self.Oy21 - Posdy
                if self.Ox11 < 220  and self.Ox11 >0 and self.TrouveVO == False :
                    distx= self.Ox11 - Posdx
                    disty=self.Oy11 - Posdy
                    c = distx**2 + disty**2
                    dist = math.sqrt(c)
                    self.gr.add_edge(depart,"O11" , weight=dist )
                    self.gr.add_edge("O11","O12" , weight=5 )

                    self.dc.DrawLine(Posdx, Posdy, self.Ox11, self.Oy11)
                self.verifierTrajectoire(Posdx,Posdy,self.Ox13,self.Oy13)
                if self.Ox13 < 220  and self.Ox13 >0 and self.TrouveVO == False :
                    distx= self.Ox22 - Posdx
                    c = distx**2 + disty**2
                    dist = math.sqrt(c)
                    self.gr.add_edge(depart,"O13" , weight=dist )
                    self.gr.add_edge("O13","O14" , weight=5 )
                    self.dc.DrawLine(Posdx, Posdy, self.Ox13, self.Oy13)
                    #Ajout des arcs
                    self.dc.DrawLine(self.Ox13, self.Oy13, self.Ox14, self.Oy14)
                self.TrouveO = True
                self.TrouveO1 = True
            b = b+1
        if self.TrouveO == False and  Posdx < 220  and Posdx > 0 :
            self.dc.DrawLine(Posdx,Posdy,Posfx,Posfy)
            self.gr.add_edge(depart,"Fin" , weight=5 )


    def verifierTrajectoire(self,Posdx,Posdy,Posfx,Posfy):
        ad = abs(Posdx-Posfx)
        bd = abs(Posdy-Posfy)
        tanA = ad/bd
        b =1
        self.TrouveVO = False
        while bd > b and self.TrouveVO ==False :
            a = (tanA * b)
            posx = a + Posdx
            posy = Posdy - b
            if posy >= self.Oy14 and posy<=self.Oy11  and posx>=self.Ox14 and posx<=self.Ox11:
                self.TrouveVO = True
            if posy >= self.Oy24 and posy<=self.Oy21  and posx>=self.Ox24 and posx<=self.Ox21:
                self.TrouveVO = True
            b = b + 1




    def __fetchCurrentPose(self):
        self.dc.Clear()

        if self.i < 5:
             self.direction=1
             self.roboty= self.roboty +10
        elif self.i < 10:
            self.direction=2
            self.robotx= self.robotx +10
        elif self.i < 15:
            self.direction=3
            self.roboty= self.roboty -10
        elif self.i < 20:
             self.direction=4
             self.robotx= self.robotx -10
        else:
            self.i = 0
        self.i=self.i+1
        self.DrawLine()
        threading.Timer(1, self.__fetchCurrentPose).start()
        #self.__send(GetPose())





class Obstacle(wx.Frame):
    def __init__( self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(300,300))
        self.initUi()
        self.bindHandlers()
        self.Show()


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

    def onAjouteClicked(self, event):
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

if __name__ == '__main__':
    app = wx.App()
    Example(None, 'Line')
    app.MainLoop()


