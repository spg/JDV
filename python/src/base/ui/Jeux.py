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

import wx
from pygraph.classes.graph import graph
from pygraph.classes.digraph import digraph
from pygraph.algorithms.searching import breadth_first_search


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(1000, 1000))
        self.panel = wx.Panel(self, -1)
        wx.FutureCall(2000, self.DrawLine)
        self.gr = graph()
        self.Centre()
        self.Show()


    def bindHandlers(self):
        self.Bind(wx.EVT_BUTTON, self.onButtonClicked, self.button)
        self.Bind(wx.EVT_BUTTON, self.onAfficheClicked, self.Affiche)

    def CreerGraph(self):
        self.gr.add_node("Depart")
        self.gr.add_node("1")
        self.gr.add_node("2")
        self.gr.add_node("3")
        self.gr.add_node("4")
        self.gr.add_node("5")
        self.gr.add_node("6")
        self.gr.add_node("7")
        self.gr.add_node("8")

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
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle(70+self.d, 10+self.d, 5, 5)
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle(130+self.d, 10+self.d, 5, 5)
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle(190+self.d, 10+self.d, 5, 5)
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle(20+self.d, 30+self.d, 5, 5)
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle(20+self.d, 60+self.d, 5, 5)
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle(190+self.d, 30+self.d, 5, 5)
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle(190+self.d, 60+self.d, 5, 5)
        # Point d'arriver pour la zone de  dessins
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle(55+self.d, 240+self.d, 5, 5)
        # Met les composant sur la fenetre
        self.button = wx.Button(self.panel, label="Obstacle", pos=(500, 500),size=(100,50))
        self.Affiche = wx.Button(self.panel, label="Affiche", pos=(700, 500),size=(100,50))
        self.bindHandlers()

    def onButtonClicked(self, event):
        #Ouvre la fenetre des obstacles
        self.O = Obstacle(self,'Obstacle')

    def onAfficheClicked(self, event):

        #Affiche les obstacle
        #x1=self.O.getx1()+self.d
        #x2=self.O.getx2()+self.d
        #y1=self.O.gety1()+self.d
        #y2=self.O.gety2()+self.d
        #Valeur par default pour bu de test
        x1=100+self.d
        x2=90+self.d
        y1=150+self.d
        y2=250+self.d
        #Affichage des obstacle
        self.dc.SetBrush(wx.Brush('#000000'))
        self.dc.DrawRectangle(x1, y1, 20, 20)
        self.dc.SetBrush(wx.Brush('#000000'))
        self.dc.DrawRectangle(x2, y2, 20, 20)
        #Affichage des noeuds des obstacle 1
        self.dc.DrawRectangle(20+x1, 20+y1, 5, 5)
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle(20+x1, y1-40, 5, 5)
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle(x1-40, 20+y1, 5, 5)
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle(x1-40, y1-40, 5, 5)
        #Affichage des noeuds des obstacle 1
        self.dc.DrawRectangle(30+x2, 10+y2, 5, 5)
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle(30+x2, y2-10, 5, 5)
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle(x2-10, 10+y2, 5, 5)
        self.dc.SetBrush(wx.Brush('#00ff00'))
        self.dc.DrawRectangle(x2-10, y2-10, 5, 5)
        #Ajout des noueds des obstacle
        #Ajout des chemein possible






        ##Algorithme maison pour trouver une trajectoire
        #Affichage de la position du robot depart
        #posxa = posxb= 20+self.d
        #posya = posyb= 20+self.d
        #self.dc.SetBrush(wx.Brush('#333333'))
        #self.dc.DrawRectangle(posxa, posya, 20, 20)
        #Affichage de la position  final
        #posfx = 20+self.d
        #posfy = 400+self.d
        #self.dc.SetBrush(wx.Brush('#444444'))
        #self.dc.DrawRectangle(posfx, posfy, 20, 20)
        #trouve1 =trouve2 =False
        #trouve=True
        #i = 0
        #posx = 0
        #posy = 0
        #while i < posfy:
            #print "La variable i vaut :%d" % i
            #si il arrive a la hauteur d un obstacle 1
            #while (trouve):
                #trouve = False
                #if (i == y1):
                    ## est ce que le robot touche l'obstacle
                    #if((posxb+20>x1)and(posxb<=(x1+60))):
                       #posyb = i
                        #posxb = x1+70
                        #trouve=True
                    #else:
                        #posyb = i
                        #si il arrive a la hauteur d un obstacle 1
                    #trouve1=True
               # if (i == y2):
                    # est ce que le robot touche l'obstacle
                    #if((posxb+20>x2)and(posxb<=(x2+60))):
                        #posyb = i
                       #posxb = x2+70
                       # trouve=True
                        #trouve2=True
                    #else:
                        #posyb = i
                        #trouve2=True
                    #trouve2=True
            #trouve=True
            #if ((trouve1==True)or (trouve2==True)):
                #self.dc.DrawLine(posxa, posya, posxb, posyb)
                #self.dc.SetBrush(wx.Brush('#333333'))
                #self.dc.DrawRectangle(posxb, posyb, 20, 20)
                #posxa= posxb
                #posya= posyb
            #if ((trouve1==True)and (trouve2==True)):

                #posxa= posfx
                #posya= posfy
            #i+=10
        #self.dc.DrawLine(posxa, posya, posxb, posyb)
        #self.dc.SetBrush(wx.Brush('#333333'))
        #self.dc.DrawRectangle(posxb, posyb, 20, 20)

    def decouperJeu(self):
    #a = []
    # for i in xrange(3):
    #     a.append([])
    #     for j in xrange(3):
    #         a[i].append(i+j)
        self.zone = []
        i=0
        while ( i== 460):
            self.zone.append([])
            j=0
        while (j == 220):
            j = j +10
            if ((i == posfx) and (j == posfy)):
                #si la case a un obstacle
                self.zone[i]=0
            else:
                #si la case est vide
                self.zone[i]=1
        i= i+10






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