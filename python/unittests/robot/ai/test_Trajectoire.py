import unittest
from python.src.base.ui.Trajectoire import  Trajectoire

class Test_Trajectoire(unittest.TestCase):

    def test_Un_Obstacle_(self):
        liste = [(175.0, 65.0), (85, 85), (55, 85), (25.0, 65.0)]
        t = Trajectoire(0,0 ,65 ,65)
        chemin = t.PathFinding(175.00, 65.00,25.00, 65.00 )
        self.assertEqual(chemin,liste)

    def test_Deux_Obstacle_(self):
        liste = [(175.0, 65.0), (120, 85), (90, 85), (70, 70), (40, 70), (25.0, 65.0)]
        t = Trajectoire(50,50 ,100 ,65)
        chemin = t.PathFinding(175.00, 65.00,25.00, 65.00 )
        self.assertEqual(chemin,liste)

    def test_Deux_Obstacle_Enver(self):
        liste = [(25.0, 65.0),(40, 70) , (70, 70), (90, 85), (120, 85), (175.0, 65.0)]
        t = Trajectoire(50,50 ,100 ,65)
        chemin = t.PathFinding(25.00, 65.00,175.00, 65.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_LigneY(self):
        liste = [(175.0, 55.0), (85, 85), (55, 85), (25.0, 55.0)]
        t = Trajectoire(65,50 ,65 ,65)
        chemin = t.PathFinding(175.00, 55.00,25.00, 55.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Coller_LigneY(self):
        liste = [(175.0, 80.0), (110, 95), (80, 95), (25.0, 80.0)]
        t = Trajectoire(90,65 ,90 ,75)
        chemin = t.PathFinding(175.00, 80.00,25.00, 80.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Lignex(self):
        liste = [(175.0, 65.0), (120, 85), (90, 85), (70, 85), (40, 85), (25.0, 65.0)]
        t = Trajectoire(100,65 ,50 ,65)
        chemin = t.PathFinding(175.00, 65.00,25.00, 65.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Coller_Lignex(self):
        liste = [(175.0, 80.0), (110, 95), (80, 95), (25.0, 80.0)]
        t = Trajectoire(100,75 ,90 ,75)
        chemin = t.PathFinding(175.00, 80.00,25.00, 80.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas1_Compliquer(self):
        liste = [(175.0, 80.0), (100, 90), (90, 70), (60, 70), (25.0, 100.0)]
        t = Trajectoire(80,110 ,70 ,90)
        chemin = t.PathFinding(175.00, 80.00,25.00, 100.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas2_Compliquer(self):
        liste = [(175.0, 105.0), (110, 80), (80, 80), (25.0, 105.0)]
        t = Trajectoire(80,110 ,90 ,100)
        chemin = t.PathFinding(175.00, 105.00,25.00, 105.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas3_Compliquer(self):
        liste = [(175.0, 105.0), (100, 90), (70, 90), (25.0, 105.0)]
        t = Trajectoire(80,110 ,90 ,110)
        chemin = t.PathFinding(175.00, 105.00,25.00, 105.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas4_Compliquer(self):
        liste = [(175.0, 80.0), (100, 80), (70, 80), (25.0, 100.0)]
        t = Trajectoire(80,100 ,90 ,100)
        chemin = t.PathFinding(175.00, 80.00,25.00, 100.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas5_Compliquer(self):
        liste = [(175.0, 60.0), (140, 90), (110, 90), (25.0, 105.0)]
        t = Trajectoire(130,50 ,120 ,70)
        chemin = t.PathFinding(175.00, 60.00,25.00, 105.00 )
        self.assertEqual(chemin,liste)


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