#!/usr/bin/python
# -*- coding: utf-8 -*-


import math
import networkx as nx
from src.base.ui.Obstacle import  Obstacle

class Trajectoire():
    def __init__(self,Departx,Departy,Finx,Finy):
        self.Envers = False
        if Departy-Finy <= 0 :
            self.Envers = True
            self.posDepartx =Finx
            self.posDeparty =Finy
            self.posFinx =Departx
            self.posFiny =Departy
        else :
            self.posDepartx =Departx
            self.posDeparty =Departy
            self.posFinx =Finx
            self.posFiny =Finy
        self.x1=140
        self.y1=250
        self.x2=140
        self.y2=150
        self.Ox21=35+self.x2
        self.Ox22=35+self.x2
        self.Ox23=self.x2-20
        self.Ox24=self.x2-20
        self.Oy21=35+self.y2
        self.Oy22=self.y2-20
        self.Oy23=35+self.y2
        self.Oy24=self.y2-20
        self.Ox11=35+self.x1
        self.Ox12=35+self.x1
        self.Ox13=self.x1-20
        self.Ox14=self.x1-20
        self.Oy11=35+self.y1
        self.Oy12=self.y1-20
        self.Oy13=35+self.y1
        self.Oy14=self.y1-20
        self.gr = nx.Graph()
        self.Trouvetrajectoire(self.posDepartx,self.posDeparty,self.posFinx,self.posFiny)
        self.grs = nx.Graph()
        self.grs = nx.shortest_path(self.gr,"Depart","Fin")
        print self.grs
        self.FaireListe()



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
        b = 1
        self.TrouveO = False
        while bd > b and self.TrouveO ==False :
            a = (tanA * b)
            posx = a + Posdx
            posy = Posdy - b
            if posy>= self.Oy24 and posy<=self.Oy21  and posx>= self.Ox24 and posx<=self.Ox21:
                # Calcule des distances
                disty=self.Oy21 - Posdy
                self.verifierTrajectoire(Posdx,Posdy,self.Ox21,self.Oy21)
                if self.Ox21 < 220  and self.Ox21 >0 and self.TrouveVO == False :
                    distx= self.Ox21 - Posdx
                    c = distx**2 + disty**2
                    dist = math.sqrt(c)
                    self.gr.add_edge(depart,"O21" , weight=dist )
                    self.gr.add_edge("O21","O22" , weight=55.00 )
                self.verifierTrajectoire(Posdx,Posdy,self.Ox23,self.Oy23)
                if self.Ox23 < 220  and self.Ox23 > 0 and self.TrouveVO == False :
                    distx= self.Ox23 - Posdx
                    c = distx**2 + disty**2
                    dist = math.sqrt(c)
                    self.gr.add_edge(depart,"O23" , weight=dist )
                    self.gr.add_edge("O23","O24" , weight=55.00 )
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
                    self.gr.add_edge("O11","O12" , weight=55.00 )
                self.verifierTrajectoire(Posdx,Posdy,self.Ox13,self.Oy13)
                if self.Ox13 < 220  and self.Ox13 >0 and self.TrouveVO == False :
                    distx= self.Ox22 - Posdx
                    c = distx**2 + disty**2
                    dist = math.sqrt(c)
                    self.gr.add_edge(depart,"O13" , weight=dist )
                    self.gr.add_edge("O13","O14" , weight=55.00 )
                self.TrouveO = True
                self.TrouveO1 = True
            b = b+1
        if self.TrouveO == False and  Posdx < 220  and Posdx > 0 :
            distx= Posfx- Posdx
            disty=Posfy- Posdy
            c = distx**2 + disty**2
            dist = math.sqrt(c)
            self.gr.add_edge(depart,"Fin" , weight=dist)


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

    def FaireListe(self):
        self.liste = []
        self.nbrelement = 0
        n1 = ""
        for n in self.grs:
            if self.Envers==True:
                self.liste.append((self.TrouverValeurX(n),self.TrouverValeurY(n)))
            else:
                self.liste.insert(0,(self.TrouverValeurX(n),self.TrouverValeurY(n)))


    def TrouverValeurX(self,point):
        if point =="Depart":
            return self.posDepartx
        elif point =="O11":
            return self.Ox11
        elif point =="O12":
            return self.Ox12
        elif point =="O13":
            return self.Ox13
        elif point =="O14":
            return self.Ox14
        elif point =="O21":
            return self.Ox21
        elif point =="O22":
            return self.Ox22
        elif point =="O23":
            return self.Ox23
        elif point =="O24":
            return self.Ox24
        elif point =="Fin":
            return self.posFinx


    def TrouverValeurY(self,point):
        if point =="Depart":
            return self.posDeparty
        elif point =="O11":
            return self.Oy11
        elif point =="O12":
            return self.Oy12
        elif point =="O13":
            return self.Oy13
        elif point =="O14":
            return self.Oy14
        elif point =="O21":
            return self.Oy21
        elif point =="O22":
            return self.Oy22
        elif point =="O23":
            return self.Oy23
        elif point =="O24":
            return self.Oy24
        elif point =="Fin":
            return self.posFiny

    def getListe(self):
        return self.liste