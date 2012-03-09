import unittest
import networkx as nx
from networkx.algorithms.shortest_paths.generic import shortest_path
from src.robot.ai.graph.node import Node

class TestNetworkx(unittest.TestCase):
    def test_simple(self):
        g = nx.Graph()

        depart = Node(0, 0, "depart")
        arrivee = Node(100, 300, "arrivee")
        b = Node(200, 40, "b")
        c = Node(50, 30, "c")

        g.add_edge(depart, c, distance=Node.distanceBetween(depart, c))
        g.add_edge(depart, b, distance=Node.distanceBetween(depart, b))
        g.add_edge(c, arrivee, distance=Node.distanceBetween(c, arrivee))
        g.add_edge(b, arrivee, distance=Node.distanceBetween(b, arrivee))

        path = shortest_path(g, depart, arrivee, "distance")

        self.assertEqual(3, len(path))

        self.assertEqual(depart, path[0])
        self.assertEqual(c, path[1])
        self.assertEqual(arrivee, path[2])
