import unittest
from python.src.base.ui.Trajectoire import  Trajectoire

class Test_Trajectoire(unittest.TestCase):

    def test_Un_Obstacle_(self):
        liste = [(350.0, 130.0), (170, 170), (110, 170), (50.0, 130.0)]
        t = Trajectoire(0,0 ,130 ,130)
        chemin = t.PathFinding(350.00, 130.00,50.00, 130.00 )
        self.assertEqual(chemin,liste)

    def test_Deux_Obstacle_(self):
        liste = [(350.0, 130.0), (240, 170), (180, 170), (140, 140), (80, 140), (50.0, 130.0)]
        t = Trajectoire(100,100 ,200 ,130)
        chemin = t.PathFinding(350.00, 130.00,50.00, 130.00 )
        self.assertEqual(chemin,liste)

    def test_Deux_Obstacle_Enver(self):
        liste = [(50.0, 130.0), (80, 140),  (140, 140),(180, 170) , (240, 170), (350.0, 130.0)]
        t = Trajectoire(100,100 ,200 ,130)
        chemin = t.PathFinding(50.00, 130.00,350.00, 130.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_LigneY(self):
        liste = [(350.0, 110.0), (170, 80), (110, 80), (50.0, 110.0)]
        t = Trajectoire(130,100 ,130 ,130)
        chemin = t.PathFinding(350.00, 110.00,50.00, 110.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Coller_LigneY(self):
        liste = [(350.0, 160.0), (220, 110), (160, 110), (50.0, 160.0)]
        t = Trajectoire(180,130 ,180 ,150)
        chemin = t.PathFinding(350.00, 160.00,50.00, 160.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Lignex(self):
        liste = [(350.0, 130.0), (240, 170), (180, 170), (140, 170), (80, 170), (50.0, 130.0)]
        t = Trajectoire(200,130 ,100 ,130)
        chemin = t.PathFinding(350.00, 130.00,50.00, 130.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Coller_Lignex(self):
        liste = [(350.0, 160.0), (240, 190), (160, 190), (50.0, 210.0)]
        t = Trajectoire(200,150 ,180 ,150)
        chemin = t.PathFinding(350.00, 160.00,50.00, 210.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas1_Compliquer(self):
        liste = [(350.0, 200.0), (200, 180), (180, 160), (120, 160), (50.0, 200.0)]
        t = Trajectoire(160,200 ,140 ,180)
        chemin = t.PathFinding(350.00, 200.00,50.00, 200.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas2_Compliquer(self):
        liste = [(350.0, 210.0), (220, 160), (160, 160), (50.0, 210.0)]
        t = Trajectoire(160,200 ,180 ,180)
        chemin = t.PathFinding(350.00, 210.00,50.00, 210.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas3_Compliquer(self):
        liste = [(350.0, 210.0), (200, 180), (140, 180), (50.0, 210.0)]
        t = Trajectoire(160,200 ,180 ,200)
        chemin = t.PathFinding(350.00, 210.00,50.00, 210.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas4_Compliquer(self):
        liste = [(350.0, 210.0), (200, 180), (140, 180), (50.0, 210.0)]
        t = Trajectoire(160,200 ,180 ,200)
        chemin = t.PathFinding(350.00, 210.00,50.00, 210.00 )
        self.assertEqual(chemin,liste)



     # test nord-sud

    def test_Un_Obstacle_x(self):
        liste = [(350.0, 200.0), (380, 200), (380, 140), (350.0, 10.0)]
        t = Trajectoire(0,0 ,340 ,160)
        chemin = t.PathFinding(350.00, 10.00,350.00, 200.00)
        self.assertEqual(chemin,liste)

    def test_Deux_Obstacle_x(self):
        liste = [(350.0, 200.0), (380, 200), (380, 140), (380, 130), (380, 70), (350.0, 10.0)]
        t = Trajectoire(340,90 ,340 ,160)
        chemin = t.PathFinding(350.00, 10.00,350.00, 200.00)
        self.assertEqual(chemin,liste)

    def test_Deux_Obstacle_Enver_x(self):
        liste = [(350.0, 10.0), (380, 70), (380, 130), (380, 140), (380, 200), (350.0, 200.0)]
        t = Trajectoire(340,90 ,340 ,160)
        chemin = t.PathFinding(350.00, 200.00,350.00, 10.00 )
        self.assertEqual(chemin,liste)


    def test_Obstacle_Coller_LigneY(self):
        liste = [(350.0, 10.0), (380, 110), (380, 190), (350.0, 200.0)]
        t = Trajectoire(340,130 ,340 ,150)
        chemin = t.PathFinding(350.00, 200.00,350.00, 10.00)
        self.assertEqual(chemin,liste)

    def test_Obstacle_Ligne0_x(self):
         liste = [(350.0, 200.0), (410, 170), (410, 110), (350.0, 10.0)]
         t = Trajectoire(370,130 ,330 ,130)
         chemin = t.PathFinding(350.00, 10.00,350.00, 200.00 )
         self.assertEqual(chemin,liste)

    def test_Obstacle_Coller_Lignex_x(self):
        liste = [(340.0, 200.0), (390, 170), (390, 110), (340.0, 10.0)]
        t = Trajectoire(350,130 ,330 ,130)
        chemin = t.PathFinding(340.00, 10.00,340.00, 200.00 )
        self.assertEqual(chemin,liste)

    def test_Cas0_Compliquer_x(self):
        liste = [(450.0, 200.0), (420, 140), (420, 80), (450.0, 10.0)]
        t = Trajectoire(440,100 ,440 ,140)
        chemin =  t.PathFinding(450.00, 10.00,450.00, 200.00)
        self.assertEqual(chemin,liste)

    def test_Cas1_Compliquer_x(self):
        liste = [(350.0, 200.0), (380, 180), (380, 80), (350.0, 10.0)]
        t = Trajectoire(340.00,140.00,340.00 ,100.00)
        chemin = t.PathFinding(350.00, 10.00,350.00, 200.00)
        self.assertEqual(chemin,liste)