#!/usr/bin/python
# -*- coding: utf-8 -*-


import math
import networkx as nx
from python.src.base.ui.Obstacle import  Obstacle

class Trajectoire():
    def __init__(self,obstacle_1_x,obstacle_1_y,obstacle_2_x,obstacle_2_y):
        self.Ox21=40+obstacle_2_x
        self.Ox22=40+obstacle_2_x
        self.Ox23=obstacle_2_x-20
        self.Ox24=obstacle_2_x-20
        self.Oy21=40+obstacle_2_y
        self.Oy22=obstacle_2_y-20
        self.Oy23=40+obstacle_2_y
        self.Oy24=obstacle_2_y-20
        self.Ox11=40+obstacle_1_x
        self.Ox12=40+obstacle_1_x
        self.Ox13=obstacle_1_x-20
        self.Ox14=obstacle_1_x-20
        self.Oy11=40+obstacle_1_y
        self.Oy12=obstacle_1_y-20
        self.Oy13=40+obstacle_1_y
        self.Oy14=obstacle_1_y-20

    def PathFinding(self,Departx,Departy,Finx,Finy):
        self.Envers = False
        if Departx-Finx < 0 :
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
        self.gr = nx.Graph()
        self.Trouvetrajectoire(self.posDepartx,self.posDeparty,self.posFinx,self.posFiny)
        self.grs = nx.Graph()
        self.grs = nx.shortest_path(self.gr,"Depart","Fin")
        print self.grs
        self.FaireListe()
        return self.liste

    def Trouvetrajectoire(self,Posdx,Posdy,Posfx,Posfy):
        self.TrouveO = True
        self.TrouveO1 = False
        self.TrouveO2 = False
        self.ParcourireLigne(Posdx,Posdy,Posfx,Posfy,"Depart")
        while(self.TrouveO == True):
            self.TrouveO=False
            if self.TrouveO1==True:
                self.TrouveO1=False
                print("Traject 1")
                self.ParcourireLigne(self.Ox14,self.Oy14,Posfx,Posfy,"O14")
                self.ParcourireLigne(self.Ox13,self.Oy13,Posfx,Posfy,"O13")
            if self.TrouveO2==True:
                print("Traject 2")
                self.TrouveO2=False
                self.ParcourireLigne(self.Ox24,self.Oy24,Posfx,Posfy,"O24")
                self.ParcourireLigne(self.Ox23,self.Oy23,Posfx,Posfy,"O23")

    def ParcourireLigne(self,Posdx,Posdy,Posfx,Posfy,depart):
        ad = abs(Posdy-Posfy)
        bd = abs(Posdx-Posfx)
        print "bd: %d" % bd
        tanA = ad/bd
        b = 1
        self.TrouveO = False
        self.TrouveVO = False
        while bd > b and self.TrouveO ==False :
            a = (tanA * b)
            posy = a + Posdy
            posx = Posdx - b
            #print "posx: %d" % posx
            #print "posy: %d" % posy

            if posy>= self.Oy24 and posy<=self.Oy21  and posx>= self.Ox24 and posx<=self.Ox21:
                print(" O2")
                # Calcule des distances
                distx=self.Ox21 - Posdx
                self.verifierTrajectoire(Posdx,Posdy,self.Ox21,self.Oy21)
                if self.Oy21 < 220  and self.Oy21 >0 and self.TrouveVO == False :
                    disty= self.Oy21 - Posdy
                    c = distx**2 + disty**2
                    dist = math.sqrt(c)
                    self.gr.add_edge(depart,"O21" , weight=dist )
                    self.gr.add_edge("O21","O23" , weight=55.00 )
                self.verifierTrajectoire(Posdx,Posdy,self.Ox22,self.Oy22)
                if self.Oy22 < 220  and self.Oy22 > 0 and self.TrouveVO == False :
                    disty= self.Oy22 - Posdy
                    c = distx**2 + disty**2
                    dist = math.sqrt(c)
                    self.gr.add_edge(depart,"O22" , weight=dist )
                    self.gr.add_edge("O22","O24" , weight=55.00 )
                self.TrouveO = True
                self.TrouveO2=True
            if posy >= self.Oy14 and posy<=self.Oy11  and posx>=self.Ox14 and posx<=self.Ox11:
                print(" O1")
                self.verifierTrajectoire(Posdx,Posdy,self.Ox11,self.Oy11)
                # Calcule des distance
                distx= self.Ox11 - Posdx
                if self.Oy11 < 220  and self.Oy11 >0 and self.TrouveVO == False :
                    disty=self.Oy11 - Posdy
                    c = distx**2 + disty**2
                    dist = math.sqrt(c)
                    self.gr.add_edge(depart,"O11" , weight=dist )
                    self.gr.add_edge("O11","O13" , weight=55.00 )
                self.verifierTrajectoire(Posdx,Posdy,self.Ox12,self.Oy12)
                if self.Oy12 < 220  and self.Oy12 >0 and self.TrouveVO == False :
                    distx= self.Ox12 - Posdx
                    c = distx**2 + disty**2
                    dist = math.sqrt(c)
                    self.gr.add_edge(depart,"O12" , weight=dist )
                    self.gr.add_edge("O12","O14" , weight=55.00 )
                self.TrouveO = True
                self.TrouveO1 = True
            b = b+1
        if self.TrouveO == False and  Posdy < 220  and Posdy > 0 :
            print("fin")
            distx= Posfx- Posdx
            disty=Posfy- Posdy
            c = distx**2 + disty**2
            dist = math.sqrt(c)
            self.gr.add_edge(depart,"Fin" , weight=dist)


    def verifierTrajectoire(self,Posdx,Posdy,Posfx,Posfy):
        ad = abs(Posdy-Posfy)
        bd = abs(Posdx-Posfx)
        tanA = ad/bd
        b =1
        self.TrouveVO = False
        while bd > b and self.TrouveVO ==False :
            a = (tanA * b)
            posy = a + Posdy
            posx = Posdx - b
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
