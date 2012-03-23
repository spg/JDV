import unittest
from python.src.robot.ai.graph.node import Node
from python.src.robot.ai.graph.simplegraph import SimpleGraph

class TestSimpleGraph(unittest.TestCase):
    def test_constructor(self):
        node1 = Node(0, 0)
        node2 = Node(1, 2)

        graph = SimpleGraph()

        graph.add_edge(node1, node2)

    def test_constructor_with_arguments_of_wrong_type(self):
        node1 = Node(0, 0)
        node2 = 3

        graph = SimpleGraph()

        self.assertRaises(TypeError, graph.add_edge, (node1, node2))

    def test_shortest_path(self):
        g = SimpleGraph()

        depart = Node(0, 0, "depart")
        arrivee = Node(100, 300, "arrivee")
        b = Node(200, 40, "b")
        c = Node(50, 30, "c")

        g.add_edge(depart, c)
        g.add_edge(depart, b)
        g.add_edge(c, arrivee)
        g.add_edge(b, arrivee)

        path = g.shortest_path(depart, arrivee)

        self.assertEqual(3, len(path))

        self.assertEqual(depart, path[0])
        self.assertEqual(c, path[1])
        self.assertEqual(arrivee, path[2])