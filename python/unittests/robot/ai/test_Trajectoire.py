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