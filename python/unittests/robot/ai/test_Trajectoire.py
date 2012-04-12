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
        liste = [(175.0, 60.0), (115, 95), (65, 95), (25.0, 105.0)]
        t = Trajectoire(90,70 ,80 ,70)
        chemin = t.PathFinding(175.00, 60.00,25.00, 105.00 )
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
        chemin = t.PathFinding(23.00, 10.00, 200.00, 100.00 )
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
        liste = [(175.0, 60.0), (155, 35), (115, 35), (25.0, 105.0)]
        t = Trajectoire(130,50 ,120 ,70)
        chemin = t.PathFinding(175.00, 60.00,25.00, 105.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas6_Compliquer(self):
        liste = [(175.0, 60.0), (155, 35), (115, 35), (25.0, 10.0)]
        t = Trajectoire(130,50 ,120 ,70)
        chemin = t.PathFinding(175.00, 60.00,25.00, 10.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas7_Compliquer(self):
        liste = [(10.0, 56.0), (69, 45), (109, 45), (173.0, 56.0)]
        t = Trajectoire(101,84 ,84 ,60)
        chemin  =t.PathFinding(10.00, 56.00, 173.00, 56.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas1(self):
        liste = [(23.0, 10.0), (69, 45), (109, 45), (200.0, 100.0)]
        t = Trajectoire(101,84 ,84 ,60)
        chemin  = t.PathFinding(23.00, 10.00, 200.00, 100.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas9(self):
        liste = [(23.0, 10.0), (69, 29), (109, 29), (200.0, 100.0)]
        t = Trajectoire(101,84 ,84 ,44)
        chemin  = t.PathFinding(23.00, 10.00, 200.00, 100.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas2(self):
        liste = [(23.0, 100.0), (69, 30), (109, 30), (126, 69), (200.0, 100.0)]
        t = Trajectoire(101,84 ,84 ,45)
        chemin  = t.PathFinding(23.00, 100.00, 200.00, 100.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas3(self):
        liste = [(23.0, 100.0), (86, 69), (126, 69), (200.0, 100.0)]
        t = Trajectoire(101,84 ,84 ,43)
        chemin  = t.PathFinding(23.00, 100.00, 200.00, 100.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas4(self):
        liste = [(23.0, 10.0), (69, 68), (109, 68), (200.0, 100.0)]
        t = Trajectoire(101,26 ,84 ,43)
        chemin  = t.PathFinding(23.00, 10.00, 200.00, 100.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas5(self):
        liste = [(23.0, 30.0), (69, 68), (109, 68), (126, 51), (200.0, 30.0)]
        t = Trajectoire(101,26 ,84 ,43)
        chemin  = t.PathFinding(23.00, 30.00, 200.00, 30.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas6(self):
        liste = [(23.0, 15.0), (69, 68), (109, 68), (126, 54), (200.0, 15.0)]
        t = Trajectoire(101,29 ,84 ,43)
        chemin  = t.PathFinding(23.00, 15.00, 200.00, 15.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas7(self):
        liste = [(23.0, 15.0), (69, 68), (109, 68), (126, 54), (200.0, 15.0)]
        t = Trajectoire(101,29 ,84 ,43)
        chemin  = t.PathFinding(23.00, 15.00, 200.00, 15.00 )
        self.assertEqual(chemin,liste)

    def test_Obstacle_Cas8(self):
        liste = [(160.0, 15.0), (175.0, 90.0)]
        t = Trajectoire(140,50 ,80 ,50)
        chemin  = liste =t.PathFinding(160.0, 15.0, 175.00, 90.00 )
        self.assertEqual(chemin,liste)

