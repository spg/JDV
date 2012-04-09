import unittest
from python.src.base.ui.Trajectoire import  Trajectoire

class Test_Trajectoire(unittest.TestCase):


    def test_Un_Obstacle_(self):
        liste = [(23.0, 65.0), (65, 50), (105, 50), (180.8, 65.0)]
        t = Trajectoire(0,0 ,80 ,65)
        chemin = t.PathFinding(23.00,65.00 ,180.8, 65.0 )
        self.assertEqual(chemin,liste)

    def test_Un_Obstacle_Sorti1(self):
        liste = [(23.0, 90.0), (65, 75), (105, 75), (180.8, 90.0)]
        t = Trajectoire(0,0 ,80 ,90)
        chemin = t.PathFinding(23.00,90.00 ,180.8, 90.0 )
        self.assertEqual(chemin,liste)

    def test_Un_Obstacle_Sorti2(self):
        liste = [(23.0, 20.0), (65, 50), (105, 50), (180.8, 20.0)]
        t = Trajectoire(300,300 ,80 ,25)
        chemin = t.PathFinding(23.00,20.00 ,180.8, 20.0 )
        self.assertEqual(chemin,liste)

    def test_Deux_Obstacle_(self):
        liste = [(23.0, 10.0), (65, 35), (105, 35), (135, 50), (175, 50), (200.0, 65.0)]
        t = Trajectoire(150,65 ,80 ,50)
        chemin = t.PathFinding(23.00, 10.00, 200.00, 65.00 )
        self.assertEqual(chemin,liste)


    def test_Deux_Obstacle_Enver(self):
        liste = [(200.0, 65.0),(175, 50) ,(135, 50) , (105, 35), (65, 35),(23.0, 10.0) ]
        t = Trajectoire(150,65 ,80 ,50)
        chemin = t.PathFinding(200.00, 65.00, 23.00, 10.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Coller_LigneY(self):
        liste = [(23.0, 65.0), (65, 35), (115, 35), (200.0, 10.0)]
        t = Trajectoire(90,50 ,80 ,50)
        chemin = t.PathFinding(23.00, 65.00, 200.00, 10.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_LigneY(self):
        liste = [(23.0, 65.0), (65, 35), (135, 35), (200.0, 10.0)]
        t = Trajectoire(110,50 ,80 ,50)
        chemin = t.PathFinding(23.00, 65.00, 200.00, 10.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Lignex(self):
        liste = [(23.0, 65.0), (65, 45), (105, 45), (200.0, 10.0)]
        t = Trajectoire(80,20 ,80 ,80)
        chemin =t.PathFinding(23.00, 65.00, 200.00, 10.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Coller_Lignex(self):
        liste = [(23.0, 100.0), (65, 75), (105, 75), (200.0, 10.0)]
        t = Trajectoire(80,40 ,80 ,50)
        chemin = t.PathFinding(23.00, 100.00, 200.00, 10.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Coller_Lignex2(self):
        liste = [(23.0, 10.0), (65, 25), (105, 25), (200.0, 100.0)]
        t = Trajectoire(80,40 ,80 ,50)
        chemin = t.PathFinding(23.00, 10.00, 200.00, 10.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas1_Compliquer(self):
        liste = [(175.0, 80.0), (105, 85), (95, 75), (55, 75), (25.0, 100.0)]
        t = Trajectoire(80,100 ,70 ,90)
        chemin = t.PathFinding(175.00, 80.00,25.00, 100.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas2_Compliquer(self):
        liste = [(175.0, 105.0), (115, 75), (75, 75), (25.0, 105.0)]
        t = Trajectoire( 90 ,90,80,100)
        chemin = t.PathFinding(175.00, 105.00,25.00, 105.00 )
        self.assertEqual(chemin,liste)


    def test_Obstacle_Cas3_Compliquer(self):
        liste = [(175.0, 105.0), (115, 85), (105, 85), (65, 85), (25.0, 105.0)]
        t = Trajectoire(90,100 ,80 ,100)
        chemin = t.PathFinding(175.00, 105.00,25.00, 105.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas4_Compliquer(self):
        liste = [(175.0, 10.0), (115, 25), (105, 25), (65, 25), (25.0, 10.0)]
        t = Trajectoire(90,0 ,80 ,0)
        chemin = t.PathFinding(175.00, 10.00,25.00, 10.00 )
        self.assertEqual(chemin,liste)


    def test_Obstacle_Cas5_Compliquer(self):
        liste = [(175.0, 60.0), (155, 75), (145, 95), (105, 95), (25.0, 105.0)]
        t = Trajectoire(130,50 ,120 ,70)
        chemin = t.PathFinding(175.00, 60.00,25.00, 105.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas6_Compliquer(self):
        liste = [(175.0, 60.0), (155, 35), (115, 35), (25.0, 10.0)]
        t = Trajectoire(130,50 ,120 ,70)
        chemin = t.PathFinding(175.00, 60.00,25.00, 10.00 )
        self.assertEqual(chemin,liste)
""" Commrny

     # test nord-sud

    def test_Un_Obstacle_x(self):
        liste = [(175.0, 100.0), (190, 100), (190, 70), (175.0, 10.0)]
        t = Trajectoire(0,0 ,170 ,80)
        chemin = t.PathFinding(175.00, 10.00,175.00, 100.00)
        self.assertEqual(chemin,liste)

    def test_Deux_Obstacle_x(self):
        liste = [(175.0, 100.0), (190, 100), (190, 70), (190, 65), (190, 35), (175.0, 10.0)]
        t = Trajectoire(170,45 ,170 ,80)
        chemin = t.PathFinding(175.00, 10.00,175.00, 100.00)
        self.assertEqual(chemin,liste)

    def test_Deux_Obstacle_Enver_x(self):
        liste = [(175.0, 10.0), (190, 35), (190, 65), (190, 70), (190, 100), (175.0, 100.0)]
        t = Trajectoire(170,45 ,170 ,80)
        chemin = t.PathFinding(175.00, 100.00,175.00, 10.00 )
        self.assertEqual(chemin,liste)


    def test_Obstacle_Coller_LigneY_x(self):
        liste = [(175.0, 100.0), (190, 85), (190, 55), (175.0, 10.0)]
        t = Trajectoire(170,65 ,170 ,75)
        chemin = t.PathFinding(175.00, 10.00,175.00, 100.00)
        self.assertEqual(chemin,liste)

    def test_Obstacle_CollerLigne_x(self):
         liste = [(175.0, 100.0), (155, 85), (155, 55), (175.0, 10.0)]
         t = Trajectoire(185,65 ,175 ,65)
         chemin = t.PathFinding(175.00, 10.00,175.00, 100.00)
         self.assertEqual(chemin,liste)

    def test_Obstacle_Lignex_x(self):
        liste = [(175.0, 100.0), (200, 85), (200, 55), (175.0, 10.0)]
        t = Trajectoire(150,65 ,180 ,65)
        chemin = t.PathFinding(175.00, 10.00,175.00, 100.00)
        self.assertEqual(chemin,liste)

    def test_Cas0_Compliquer_x(self):
        liste = [(225.0, 100.0), (200, 70), (200, 40), (225.0, 10.0)]
        t = Trajectoire(220,50 ,220 ,60)
        chemin =  t.PathFinding(225.00, 10.00,225.00, 100.00)
        self.assertEqual(chemin,liste)

    def test_Cas1_Compliquer_x(self):
        liste = [(175.0, 10.0), (190, 40), (190, 70), (175.0, 100.0)]
        t = Trajectoire(170.00,70.00,170.00 ,50.00)
        chemin = t.PathFinding(175.00, 100.00,175.00, 10.00)
        self.assertEqual(chemin,liste)
    """