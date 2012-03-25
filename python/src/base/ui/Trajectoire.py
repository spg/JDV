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
        self.grs = nx.shortest_path(self.gr,"Depart","Fin",weight=True)
        print self.grs
        self.FaireListe()
        print self.liste
        return self.liste

    def Trouvetrajectoire(self,Posdx,Posdy,Posfx,Posfy):
        self.TrouveO = True
        self.TrouveO11 = False
        self.TrouveO12 = False
        self.TrouveO21 = False
        self.TrouveO22 = False
        self.ParcourireLigne(Posdx,Posdy,Posfx,Posfy,"Depart")
        while(self.TrouveO == True):
            self.TrouveO=False
            if self.TrouveO11==True:
                self.TrouveO11=False
                print("Traject 13")
                self.ParcourireLigne(self.Ox13,self.Oy13,Posfx,Posfy,"O13")
            if self.TrouveO12==True:
                self.TrouveO12=False
                print("Traject 14")
                self.ParcourireLigne(self.Ox14,self.Oy14,Posfx,Posfy,"O14")

            if self.TrouveO22==True:
                print("Traject 24")
                self.TrouveO22=False
                self.ParcourireLigne(self.Ox24,self.Oy24,Posfx,Posfy,"O24")
            if self.TrouveO21==True:
                print("Traject 23")
                self.TrouveO21=False
                self.ParcourireLigne(self.Ox23,self.Oy23,Posfx,Posfy,"O23")

    def ParcourireLigne(self,Posdx,Posdy,Posfx,Posfy,depart):
        ad = Posfy-Posdy
        bd = Posdx-Posfx
        print "bd: %d" % bd
        if bd ==0:
            bd = bd+1
        tanA = ad/bd
        b = 1
        self.TrouveO = False
        while bd > b and self.TrouveO ==False :
            a = (tanA * b)
            posy = a + Posdy
            posx = Posdx - b
            #print "posx: %d" % posx
           # print "posy: %d" % posy

            if posy>= self.Oy24 and posy<=self.Oy21  and posx>= self.Ox24 and posx<=self.Ox21:
                print(" O2")
                # Calcule des distances
                distx=self.Ox21 - Posdx
                Colision21 = self.verifierTrajectoire(self.Ox21,self.Oy21,self.Ox23,self.Oy23,2)
                TrouveVO21 = self.verifierTrajectoire(Posdx,Posdy,self.Ox21,self.Oy21,0)
                Sortie21 = self.EstSortie(self.Oy21)
                if Sortie21==False and TrouveVO21 == False and Colision21 == False:
                    disty= self.Oy21 - Posdy
                    c = distx**2 + disty**2
                    dist = math.sqrt(c)
                    self.gr.add_edge("O21","O23" , weight=55.00 )
                    self.gr.add_edge(depart,"O21" , weight=dist )
                    self.TrouveO = True
                    self.TrouveO21=True
                TrouveVO22=self.verifierTrajectoire(Posdx,Posdy,self.Ox22,self.Oy22,0)
                Colision22=self.verifierTrajectoire(self.Ox22,self.Oy22,self.Ox24,self.Oy24,2)
                Sortie22 = self.EstSortie(self.Oy22)
                if Sortie22==False and TrouveVO22 == False and Colision22 == False:
                    disty= self.Oy22 - Posdy
                    c = distx**2 + disty**2
                    dist = math.sqrt(c)
                    self.gr.add_edge(depart,"O22" , weight=dist )
                    self.gr.add_edge("O22","O24" , weight=55.00 )
                    self.TrouveO = True
                    self.TrouveO22=True
                if  Colision21 and Colision22 and Sortie21 == False and  Sortie22 == False :
                    disty=self.Oy21 - Posdy
                    c = distx**2 + disty**2
                    dist = math.sqrt(c)
                    self.gr.add_edge(depart,"O21" , weight=dist )
                    disty=self.Oy22 - Posdy
                    c = distx**2 + disty**2
                    dist = math.sqrt(c)
                    self.gr.add_edge(depart,"O22" , weight=dist )
                    dist = self.Ox21 - self.Ox13
                    self.gr.add_edge("O21","O13" , weight=dist)
                    self.gr.add_edge("O22","O14" , weight=dist)
                    self.TrouveO = True
                    self.TrouveO11 = True
                    self.TrouveO12 = True
                if  (Colision21 and Sortie22):
                    print "Perdu"
                    if Sortie21 == False:
                        TrouveTO12 =self.verifierTrajectoire(self.Ox11,self.Ox11,self.Ox12,self.Oy12,0)
                        if TrouveTO12 == False:
                            print "Pas sortie 21"
                            disty= self.Oy21 - Posdy
                            c = distx**2 + disty**2
                            dist = math.sqrt(c)
                            self.gr.add_edge(depart,"O21" , weight=dist)
                            disty= self.Oy11 - self.Oy21
                            c = distx**2 + disty**2
                            dist = math.sqrt(c)
                            self.gr.add_edge("O21","O11" , weight=dist)
                            self.gr.add_edge("O11","O13" , weight=55.00)
                            self.TrouveO = True
                            self.TrouveO11 = True
                        else:
                            disty= self.Oy12 - Posdy
                            c = distx**2 + disty**2
                            dist = math.sqrt(c)
                            self.gr.add_edge(depart,"O12" , weight=dist)
                            self.gr.add_edge("O12","O14" , weight=dist)
                            self.TrouveO12 = True
                if Colision22 and Sortie21:
                    if Sortie22 == False:
                        print "Pas sortie 22"
                        TrouveTO22 =self.verifierTrajectoire(self.Ox22,self.Oy22,self.Ox12,self.Oy12,0)

                        if TrouveTO22 == False:
                            disty= self.Oy22 - Posdy
                            c = distx**2 + disty**2
                            dist = math.sqrt(c)
                            self.gr.add_edge(depart,"O22" , weight=dist)
                            disty=  self.Oy12- self.Oy22
                            c = distx**2 + disty**2
                            dist = math.sqrt(c)
                            self.gr.add_edge("O22","O12" , weight=dist)
                            self.gr.add_edge("O12","O14" , weight=40.00 )
                            self.TrouveO = True
                            self.TrouveO12 = True
                        else:
                            disty= self.Oy12 - Posdy
                            c = distx**2 + disty**2
                            dist = math.sqrt(c)
                            self.gr.add_edge(depart,"O12" , weight=dist)
                            self.gr.add_edge("O12","O14" , weight=dist)
                            self.TrouveO = True
                            self.TrouveO12 = True
            if posy >= self.Oy14 and posy<=self.Oy11  and posx>=self.Ox14 and posx<=self.Ox11:
                print(" O1")
                TrouveVO11 =self.verifierTrajectoire(Posdx,Posdy,self.Ox11,self.Oy11,0)
                Colision11 =self.verifierTrajectoire(self.Ox11,self.Oy11,self.Ox13,self.Oy13,1)
                # Calcule des distance
                distx= self.Ox11 - Posdx
                Sortie11 = self.EstSortie(self.Oy11)
                if Sortie11==False and TrouveVO11 == False and Colision11 == False:
                    disty=self.Oy11 - Posdy
                    c = distx**2 + disty**2
                    dist = math.sqrt(c)
                    self.gr.add_edge(depart,"O11" , weight=dist )
                    self.gr.add_edge("O11","O13" , weight=40.00 )
                    self.TrouveO = True
                    self.TrouveO11 = True
                TrouveVO12 =self.verifierTrajectoire(Posdx,Posdy,self.Ox12,self.Oy12,0)
                Colision12 =self.verifierTrajectoire(self.Ox12,self.Oy12,self.Ox14,self.Oy14,1)
                Sortie12 = self.EstSortie(self.Oy12)
                if Sortie12==False and TrouveVO12 == False and Colision12 == False:
                    disty= self.Ox12 - Posdy
                    c = distx**2 + disty**2
                    dist = math.sqrt(c)
                    self.gr.add_edge(depart,"O12" , weight=dist )
                    self.gr.add_edge("O12","O14" , weight=40.00 )
                    self.TrouveO = True
                    self.TrouveO12 = True
                if  Colision11 and Colision12 and Sortie11 == False and  Sortie12 == False :
                    disty=self.Oy11 - Posdy
                    c = distx**2 + disty**2
                    dist = math.sqrt(c)
                    print "distanc O11: %d" % dist
                    self.gr.add_edge(depart,"O12" , weight=dist )
                    disty=self.Oy12 - Posdy
                    c = distx**2 + disty**2
                    dist = math.sqrt(c)
                    print "distanc O12: %d" % dist
                    self.gr.add_edge(depart,"O11" , weight=dist )
                    dist = self.Ox11 - self.Ox23
                    self.gr.add_edge("O11","O23" , weight=dist)
                    print "distanc O23: %d" % dist
                    self.gr.add_edge("O12","O24" , weight=dist)
                    print "distanc O24: %d" % dist
                    self.TrouveO = True
                    self.TrouveO21 = True
                    self.TrouveO22 = True
                if  (Colision11 and Sortie12)or(Colision12 and Sortie11):
                    if Sortie11 == False:
                        print "Pas sortie 11"
                        TrouveTO12 =self.verifierTrajectoire(self.Ox11,self.Ox11,self.Ox12,self.Oy12,0)
                        if TrouveTO12 == False:
                            disty= self.Oy11 - Posdy
                            c = distx**2 + disty**2
                            dist = math.sqrt(c)
                            self.gr.add_edge(depart,"O11" , weight=dist)
                            disty= self.Oy11 - self.Oy21
                            c = distx**2 + disty**2
                            dist = math.sqrt(c)
                            self.gr.add_edge("O11","O21" , weight=dist)
                            self.gr.add_edge("O21","O23" , weight=40.00)
                            self.TrouveO = True
                            self.TrouveO21 = True
                        else:
                            disty= self.Oy21 - Posdy
                            c = distx**2 + disty**2
                            dist = math.sqrt(c)
                            self.gr.add_edge(depart,"O22" , weight=dist)
                            self.gr.add_edge("O22","O24" , weight=dist)
                            self.TrouveO22 = True
                    if Sortie12 == False:
                        print "Pas sortie 12"
                        disty= self.Oy22 - Posdy
                        c = distx**2 + disty**2
                        dist = math.sqrt(c)
                        self.gr.add_edge(depart,"O12" , weight=dist)
                        disty=  self.Oy12- self.Oy22
                        c = distx**2 + disty**2
                        dist = math.sqrt(c)
                        self.gr.add_edge("O12","O22" , weight=dist)
                        self.gr.add_edge("O22","O24" , weight=40.00 )
                        self.TrouveO = True
                        self.TrouveO22 = True
            b = b+1
        if self.TrouveO == False and  Posdy < 220  and Posdy > 0 :
            print("fin")

            distx= Posfx- Posdx
            disty=Posfy- Posdy
            c = distx**2 + disty**2
            dist = math.sqrt(c)
            print "distanc O2: %d" % dist
            self.gr.add_edge(depart,"Fin" , weight=dist)


    def EstSortie(self,Position):
        if Position < 220  and Position >0:
            return False
        else:
            print "Sorite"
            return True

    def verifierTrajectoire(self,Posdx,Posdy,Posfx,Posfy,obstacle):
        ad = Posdy-Posfy
        bd = Posdx-Posfx
        if bd ==0:
            bd = bd+1
        tanA = ad/bd
        b =1
        bd = abs(Posdx-Posfx)
        self.TrouveVO = False
        while bd > b :
            a = (tanA * b)
            posy = a + Posdy
            posx = Posdx - b
            if obstacle!=1:
                if posy >= self.Oy14 and posy<=self.Oy11  and posx>=self.Ox14 and posx<=self.Ox11:
                    print "O1Autre"
                    return  True
            if obstacle!=2:
                if posy >= self.Oy24 and posy<=self.Oy21  and posx>=self.Ox24 and posx<=self.Ox21:
                    print "O2Autre"
                    return  True
            b = b + 1
        return False

    def FaireListe(self):
        self.liste = []
        self.nbrelement = 0
        n1 = ""
        for n in self.grs:
            if self.Envers==False:
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

    def getgr(self):
        return self.gr