#!/usr/bin/python
# -*- coding: utf-8 -*-


import math
import networkx as nx

class Trajectoire():
    def __init__(self,obstacle_1_x,obstacle_1_y,obstacle_2_x,obstacle_2_y):
        self.obstacle_1_x = obstacle_1_x
        self.obstacle_1_y = obstacle_1_y
        self.obstacle_2_x = obstacle_2_x
        self.obstacle_2_y = obstacle_2_y

    def setObstacle(self,obstacle_1_x,obstacle_1_y,obstacle_2_x,obstacle_2_y):
        gap = 15
        gap2 = gap +10
        self.Ox21=gap2+obstacle_2_x
        self.Ox22=gap2+obstacle_2_x
        self.Ox23=obstacle_2_x-gap
        self.Ox24=obstacle_2_x-gap
        self.Oy21=gap2+obstacle_2_y
        self.Oy22=obstacle_2_y-gap
        self.Oy23=gap2+obstacle_2_y
        self.Oy24=obstacle_2_y-gap
        self.Ox11=gap2+obstacle_1_x
        self.Ox12=gap2+obstacle_1_x
        self.Ox13=obstacle_1_x-gap
        self.Ox14=obstacle_1_x-gap
        self.Oy11=gap2+obstacle_1_y
        self.Oy12=obstacle_1_y-gap
        self.Oy13=gap2+obstacle_1_y
        self.Oy14=obstacle_1_y-gap

    def InitialisationChemin(self,Departx,Departy,Finx,Finy):
        self.Envers = False
        self.Inverse = False
        if Departx-Finx == 0 and Departy-Finy <= 0 :
            self.Inverse = True
            self.posDepartx =Finy
            self.posDeparty =Finx
            self.posFinx = Departy
            self.posFiny =Departx
            self.setObstacle(self.obstacle_1_y,self.obstacle_1_x,self.obstacle_2_y,self.obstacle_2_x)
            self.SortieMax = 216
        elif Departx-Finx == 0 and Departy-Finy > 0 :
            self.Inverse = True
            self.Envers = True
            self.posDepartx =Departy
            self.posDeparty =Departx
            self.posFinx = Finy
            self.posFiny =Finx
            self.setObstacle(self.obstacle_1_y,self.obstacle_1_x,self.obstacle_2_y,self.obstacle_2_x)
            self.SortieMax = 216
        elif Departx-Finx < 0 :
            self.Envers = True
            self.posDepartx =Finx
            self.posDeparty =Finy
            self.posFinx =Departx
            self.posFiny =Departy
            self.setObstacle(self.obstacle_1_x,self.obstacle_1_y,self.obstacle_2_x,self.obstacle_2_y)
            self.SortieMax = 96
        elif Departx-Finx > 0:
            self.posDepartx =Departx
            self.posDeparty =Departy
            self.posFinx =Finx
            self.posFiny =Finy
            self.setObstacle(self.obstacle_1_x,self.obstacle_1_y,self.obstacle_2_x,self.obstacle_2_y)
            self.SortieMax = 96


    def PathFinding(self,Departx,Departy,Finx,Finy):
        self.InitialisationChemin(Departx,Departy,Finx,Finy)
        self.gr = nx.Graph()
        self.Trouvetrajectoire(self.posDepartx,self.posDeparty,self.posFinx,self.posFiny)
        self.grs = nx.Graph()
        self.grs = nx.shortest_path(self.gr,"Depart","Fin","weight")
        print self.grs
        self.FaireListe()
        print self.liste
        return self.liste

    def Trouvetrajectoire(self,Posdx,Posdy,Posfx,Posfy):
        self.TrouveO = True
        self.TrouveO11 = False
        self.TrouveO12 = False
        self.TrouveO13 = False
        self.TrouveO14 = False
        self.TrouveO21 = False
        self.TrouveO22 = False
        self.TrouveO23 = False
        self.TrouveO24 = False
        self.ParcourireLigne(Posdx,Posdy,Posfx,Posfy,"Depart")
        while(self.TrouveO == True):
            self.TrouveO=False
            if self.TrouveO11==True:
                print("Traject 11")
                self.ParcourireLigne(self.Ox11,self.Oy11,Posfx,Posfy,"O11")
            if self.TrouveO12==True:
                print("Traject 12")
                self.ParcourireLigne(self.Ox12,self.Oy12,Posfx,Posfy,"O12")
            if self.TrouveO13==True:
                print("Traject 13")
                self.ParcourireLigne(self.Ox13,self.Oy13,Posfx,Posfy,"O13")
            if self.TrouveO14==True:
                print("Traject 14")
                self.ParcourireLigne(self.Ox14,self.Oy14,Posfx,Posfy,"O14")
            if self.TrouveO21==True:
                print("Traject 21")
                self.ParcourireLigne(self.Ox21,self.Oy21,Posfx,Posfy,"O21")
            if self.TrouveO22==True:
                print("Traject 22")
                self.ParcourireLigne(self.Ox22,self.Oy22,Posfx,Posfy,"O22")
            if self.TrouveO24==True:
                print("Traject 24")
                self.ParcourireLigne(self.Ox24,self.Oy24,Posfx,Posfy,"O24")
            if self.TrouveO23==True:
                print("Traject 23")
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
                Sortie21 = self.EstSortie(self.Oy21)
                Sortie22 = self.EstSortie(self.Oy22)
                Sortie12 = self.EstSortie(self.Oy12)
                Sortie11 = self.EstSortie(self.Oy11)
                distx=self.Ox21 - Posdx
                Colision21 = self.verifierTrajectoire(self.Ox21,self.Oy21,self.Ox23,self.Oy23,2)
                TrouveVO21 = self.verifierTrajectoire(Posdx,Posdy,self.Ox21,self.Oy21,0)
                if Sortie21==False and TrouveVO21 == False and Colision21 == False:
                    dist = self.CalculeDiagonal(distx,self.Oy21 - Posdy)
                    self.gr.add_edge(depart,"O21" , weight=dist )
                    dist = self.Ox21-self.Ox23
                    self.gr.add_edge("O21","O23" , weight=dist )
                    self.TrouveO = True
                    self.TrouveO23=True
                    if (Posdy-self.Oy21) >= 0:
                        dist = self.CalculeDiagonal(distx,self.Oy21 - Posdy)
                        self.gr.add_edge(depart,"O21" , weight=dist )
                        self.TrouveO = True
                        self.TrouveO21=True
                        self.TrouveO23 =False
                TrouveVO22=self.verifierTrajectoire(self.Ox22,self.Oy22,Posdx,Posdy,2)
                Colision22=self.verifierTrajectoire(self.Ox22,self.Oy22,self.Ox24,self.Oy24,2)
                if Sortie22==False and TrouveVO22 == False and Colision22 == False:
                    dist = self.CalculeDiagonal(distx,self.Oy22 - Posdy)
                    self.gr.add_edge(depart,"O22" , weight=dist )
                    dist = self.Ox22-self.Ox24
                    self.gr.add_edge("O22","O24" , weight=dist )
                    self.TrouveO = True
                    self.TrouveO24=True
                    if (Posdy-self.Oy22) >= 0:
                        dist = self.CalculeDiagonal(distx,self.Oy22 - Posdy)
                        self.gr.add_edge(depart,"O22" , weight=dist )
                        self.TrouveO = True
                        self.TrouveO22=True
                        self.TrouveO24 =False
                if  Colision21 and Colision22 and Sortie21 == False and  Sortie22 == False :
                    dist = self.CalculeDiagonal(distx,self.Oy21 - Posdy)
                    self.gr.add_edge(depart,"O21" , weight=dist )
                    dist = self.CalculeDiagonal(distx,self.Oy22 - Posdy)
                    self.gr.add_edge(depart,"O22" , weight=dist )
                    dist = self.Ox21 - self.Ox13
                    self.gr.add_edge("O21","O13" , weight=dist)
                    self.gr.add_edge("O22","O14" , weight=dist)
                    self.TrouveO = True
                    self.TrouveO13 = True
                    self.TrouveO14 = True
                if  Colision21 and Sortie21==False and self.TrouveO13 == False:
                    print "Colisiont 21"
                    if Sortie11==False :
                        dist = self.CalculeDiagonal(distx,self.Oy11 - Posdy)
                        self.gr.add_edge(depart,"O11" , weight=dist)
                        dist = self.Ox11-self.Ox13
                        self.gr.add_edge("O11","O13" , weight=dist)
                        self.TrouveO = True
                        self.TrouveO13 = True
                if  Colision22 and Sortie22==False and self.TrouveO14 == False:
                    print "Colisiont 22"
                    if Sortie12==False:
                        dist = self.CalculeDiagonal(distx,self.Oy12 - Posdy)
                        self.gr.add_edge(depart,"O12" , weight=dist)
                        dist = self.Ox12-self.Ox14
                        self.gr.add_edge("O12","O14" , weight=dist)
                        self.TrouveO = True
                        self.TrouveO14 = True
                    else :
                        dist = self.CalculeDiagonal(distx,self.Oy21 - Posdy)
                        self.gr.add_edge(depart,"O21" , weight=dist)
                        dist = self.Ox21-self.Ox23
                        self.gr.add_edge("O21","O23" , weight=dist)
                        self.TrouveO = True
                        self.TrouveO23 = True
                    if abs(self.Ox24 - self.Ox11) < 10  and abs(self.Oy11 - self.Oy24)< 2 :
                        print "truc"
                        dist = self.CalculeDiagonal(distx,self.Oy21-Posdy)
                        self.gr.add_edge(depart,"O22" , weight=dist)
                        dist = self.CalculeDiagonal(distx,self.Oy21-self.Oy23)
                        self.gr.add_edge("O22","O24" , weight=dist)
                        dist = abs(self.Ox23 - self.Ox14)
                        self.gr.add_edge("O24","O13" , weight=dist)
                        self.TrouveO13 = True
                        self.TrouveO = True
                if  Colision21 and Sortie22:
                    print "Perdu"
                    if Sortie21 == False:
                        TrouveTO12 =self.verifierTrajectoire(self.Ox21,self.Ox21,self.Ox12,self.Oy12,0)
                        if TrouveTO12 == False:
                            print "Pas sortie 21"
                            dist = self.CalculeDiagonal(distx,self.Oy21 - Posdy)
                            self.gr.add_edge(depart,"O21" , weight=dist)
                            dist = self.CalculeDiagonal(distx,self.Oy11 - self.Oy21)
                            self.gr.add_edge("O21","O11" , weight=dist)
                            dist = self.Ox11-self.Ox13
                            self.gr.add_edge("O11","O13" , weight=dist)
                            self.TrouveO = True
                            self.TrouveO13 = True
                        else:
                            dist = self.CalculeDiagonal(distx,self.Oy12 - Posdy)
                            self.gr.add_edge(depart,"O11" , weight=dist)
                            dist = self.Ox12-self.Ox14
                            self.gr.add_edge("O11","O13" , weight=dist)
                            self.TrouveO
                            self.TrouveO13 = True
                        if abs(self.Ox23 - self.Ox12) < 10  and abs(self.Oy12 - self.Oy23)< 2 :
                            print "truc"
                            dist = self.CalculeDiagonal(distx,self.Oy21-Posdy)
                            self.gr.add_edge(depart,"O21" , weight=dist)
                            dist = self.CalculeDiagonal(distx,self.Oy21-self.Oy23)
                            self.gr.add_edge("O21","O23" , weight=dist)
                            dist = abs(self.Ox23 - self.Ox14)
                            self.gr.add_edge("O23","O14" , weight=dist)
                            self.TrouveO14 = True
                            self.TrouveO = True
                if Colision22 and Sortie21:
                    if Sortie22 == False:
                        print "Pas sortie 22"
                        TrouveTO22 =self.verifierTrajectoire(self.Ox22,self.Oy22,self.Ox12,self.Oy12,0)
                        if TrouveTO22 == False:
                            dist = self.CalculeDiagonal(distx,self.Oy22 - Posdy)
                            self.gr.add_edge(depart,"O22" , weight=dist)
                            dist = self.CalculeDiagonal(distx,self.Oy12- self.Oy22)
                            self.gr.add_edge("O22","O12" , weight=dist)
                            dist = self.Ox12-self.Ox14
                            self.gr.add_edge("O12","O14" , weight=dist)
                            self.TrouveO = True
                            self.TrouveO14 = True
                        else:
                            dist = self.CalculeDiagonal(distx,self.Oy12 - Posdy)
                            self.gr.add_edge(depart,"O12" , weight=dist)
                            dist = self.Ox12-self.Ox14
                            self.gr.add_edge("O12","O14" , weight=dist)
                            self.TrouveO = True
                            self.TrouveO14 = True
                        if abs(self.Ox13 - self.Ox22) < 7 and abs(self.Oy22 - self.Oy13)< 2 :
                                dist = self.CalculeDiagonal(distx,self.Oy11-Posdy)
                                self.gr.add_edge(depart,"O11" , weight=dist)
                                dist = self.CalculeDiagonal(distx,self.Oy11-self.Oy13)
                                self.gr.add_edge("O11","O13" , weight=dist)
                                dist = abs(self.Ox13 - self.Ox24)
                                self.gr.add_edge("O13","O24" , weight=dist)
                                self.TrouveO24 = True
                                self.TrouveO = True
            if posy >= self.Oy14 and posy<=self.Oy11  and posx>=self.Ox14 and posx<=self.Ox11:
                print(" O1")
                Sortie21 = self.EstSortie(self.Oy21)
                Sortie22 = self.EstSortie(self.Oy22)
                Sortie12 = self.EstSortie(self.Oy12)
                Sortie11 = self.EstSortie(self.Oy11)
                TrouveVO11 =self.verifierTrajectoire(Posdx,Posdy,self.Ox11,self.Oy11,0)
                Colision11 =self.verifierTrajectoire(self.Ox11,self.Oy11,self.Ox13,self.Oy13,1)
                print Colision11
                # Calcule des distance
                distx= self.Ox11 - Posdx
                if Sortie11==False and TrouveVO11 == False and Colision11 == False:
                    dist = self.CalculeDiagonal(distx,self.Oy11 - Posdy)
                    print dist
                    self.gr.add_edge(depart,"O11" , weight=dist )
                    dist = self.Ox11-self.Ox13
                    self.gr.add_edge("O11","O13" , weight=dist )
                    self.TrouveO = True
                    self.TrouveO13 = True
                    if (Posdy-self.Oy11) >= 0:
                        dist = self.CalculeDiagonal(distx,self.Oy11 - Posdy)
                        self.gr.add_edge(depart,"O11" , weight=dist )
                        self.TrouveO = True
                        self.TrouveO11=True
                        self.TrouveO13 =False
                TrouveVO12 =self.verifierTrajectoire(self.Ox12,self.Oy12,Posdx,Posdy,1)
                Colision12 =self.verifierTrajectoire(self.Ox12,self.Oy12,self.Ox14,self.Oy14,1)
                print "Colision 12 ="
                print Colision12
                print "Sortie 12 ="
                print Sortie12
                print "TrouveVO12 ="
                print TrouveVO12
                if Sortie12==False and TrouveVO12 == False and Colision12 == False:
                    dist = self.CalculeDiagonal(distx,self.Oy12 - Posdy)
                    print dist
                    self.gr.add_edge(depart,"O12" , weight=dist)
                    dist = self.Ox12-self.Ox14
                    self.gr.add_edge("O12","O14" , weight=dist )
                    self.TrouveO = True
                    self.TrouveO14 = True
                    if (Posdy-self.Oy12) >= 0:
                        dist = self.CalculeDiagonal(distx,self.Oy12 - Posdy)
                        self.gr.add_edge(depart,"O12" , weight=dist )
                        self.TrouveO = True
                        self.TrouveO12=True
                        self.TrouveO14 =False
                if  Colision11 and Colision12 and Sortie11 == False and  Sortie12 == False :
                    dist = self.CalculeDiagonal(distx,self.Oy12 - Posdy)
                    self.gr.add_edge(depart,"O12" , weight=dist )
                    dist = self.CalculeDiagonal(distx,self.Oy11 - Posdy)
                    self.gr.add_edge(depart,"O11" , weight=dist )
                    dist = self.Ox11 - self.Ox23
                    self.gr.add_edge("O11","O23" , weight=dist)
                    self.gr.add_edge("O12","O24" , weight=dist)
                    self.TrouveO = True
                    self.TrouveO23 = True
                    self.TrouveO24 = True
                if  Colision11 and Sortie12==False:
                    print "Colisiont 11"
                    if Sortie21==False :
                        dist = self.CalculeDiagonal(distx,self.Oy21 - Posdy)
                        print dist
                        self.gr.add_edge(depart,"O21" , weight=dist)
                        dist = self.Ox21-self.Ox23
                        print dist
                        self.gr.add_edge("O21","O23" , weight=dist)
                        self.TrouveO = True
                        self.TrouveO23 = True
                    if abs(self.Ox13 - self.Ox22) < 7  :
                        print "Truc"
                        dist = self.CalculeDiagonal(distx,self.Oy11-Posdy)
                        self.gr.add_edge(depart,"O11" , weight=dist)
                        dist = self.CalculeDiagonal(distx,self.Oy11-self.Oy13)
                        self.gr.add_edge("O11","O13" , weight=dist)
                        dist = abs(self.Ox13 - self.Ox24)
                        self.gr.add_edge("O13","O24" , weight=dist)
                        self.TrouveO24 = True
                        self.TrouveO = True
                if  Colision12 and Sortie11==False and self.TrouveO24==False :
                    print "Colisiont 12"
                    dist = self.CalculeDiagonal(distx,self.Oy22 - Posdy)
                    self.gr.add_edge(depart,"O22" , weight=dist)
                    dist = self.Ox22-self.Ox24
                    self.gr.add_edge("O22","O24" , weight=dist)
                    self.TrouveO = True
                    self.TrouveO24 = True
                if  (Colision11 and Sortie12)or(Colision12 and Sortie11):
                    if Sortie11 == False:
                        print "Pas sortie 11"
                        TrouveTO12 =self.verifierTrajectoire(self.Ox11,self.Ox11,self.Ox12,self.Oy12,0)
                        if TrouveTO12 == False:
                            dist = self.CalculeDiagonal(distx,self.Oy11 - Posdy)
                            self.gr.add_edge(depart,"O11" , weight=dist)
                            dist = self.CalculeDiagonal(distx,self.Oy11 - self.Oy21)
                            self.gr.add_edge("O11","O21" , weight=dist)
                            dist = self.Ox21-self.Ox23
                            self.gr.add_edge("O21","O23" , weight=dist)
                            self.TrouveO = True
                            self.TrouveO23 = True
                        else:
                            dist = self.CalculeDiagonal(distx,self.Oy21-Posdy)
                            self.gr.add_edge(depart,"O22" , weight=dist)
                            self.gr.add_edge("O22","O24" , weight=dist)
                            self.TrouveO24 = True
                        if Colision12:
                            if abs(self.Ox14 - self.Ox21) < 7 and abs(self.Oy21 - self.Oy14)< 2 :
                                dist = self.CalculeDiagonal(distx,self.Oy12-Posdy)
                                self.gr.add_edge(depart,"O12" , weight=dist)
                                dist = self.CalculeDiagonal(distx,self.Oy11-self.Oy13)
                                self.gr.add_edge("O12","O14" , weight=dist)
                                dist = abs(self.Ox14 - self.Ox23)
                                self.gr.add_edge("O14","O23" , weight=dist)
                                self.TrouveO24 = True
                                self.TrouveO = True
                        if Colision11:
                            if abs(self.Ox13 - self.Ox22) < 7 and abs(self.Oy22 - self.Oy13)< 2 :
                                dist = self.CalculeDiagonal(distx,self.Oy11-Posdy)
                                self.gr.add_edge(depart,"O11" , weight=dist)
                                dist = self.CalculeDiagonal(distx,self.Oy11-self.Oy13)
                                self.gr.add_edge("O11","O13" , weight=dist)
                                dist = abs(self.Ox13 - self.Ox24)
                                self.gr.add_edge("O13","O24" , weight=dist)
                                self.TrouveO24 = True
                                self.TrouveO = True
                    if Sortie12 == False:
                        dist = self.CalculeDiagonal(distx,self.Oy22 - Posdy)
                        self.gr.add_edge(depart,"O12" , weight=dist)
                        dist = self.CalculeDiagonal(distx,self.Oy12- self.Oy22)
                        self.gr.add_edge("O12","O22" , weight=dist)
                        dist = self.Ox22-self.Ox24
                        self.gr.add_edge("O22","O24" , weight=dist )
                        self.TrouveO = True
                        self.TrouveO24 = True
            b = b+1
        if self.TrouveO == False :
            print("fin")
            dist = self.CalculeDiagonal(Posfx- Posdx,Posfy- Posdy)
            print dist
            self.gr.add_edge(depart,"Fin" , weight=dist)



    def EstSortie(self,Position):
        if Position < self.SortieMax  and Position >15:
            return False
        else:
            print "Sortie"
            return True

    def verifierTrajectoire(self,Posdx,Posdy,Posfx,Posfy,obstacle):

        ad = Posdy-Posfy
        bd = Posdx-Posfx
        if bd ==0:
            bd = bd+1
        tanA = ad/bd
        b =1
        bd = abs(Posdx-Posfx)
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
            if self.Envers==False and self.Inverse==False:
                self.liste.append((self.TrouverValeurX(n),self.TrouverValeurY(n)))
            if self.Envers==False and self.Inverse==True:
                self.liste.append((self.TrouverValeurY(n),self.TrouverValeurX(n)))
            if self.Envers==True and self.Inverse==True:
                self.liste.insert(0,(self.TrouverValeurY(n),self.TrouverValeurX(n)))
            if self.Envers==True and self.Inverse==False:
                self.liste.insert(0,(self.TrouverValeurX(n),self.TrouverValeurY(n)))


    def CalculeDiagonal(self,x,y):
        c = x**2 + y**2
        return math.sqrt(c)

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