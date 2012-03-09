import unittest
import math
from src.robot.ai.graph.node import Node

class TestNode(unittest.TestCase):
    def test_distanceBetween(self):
        node1 = Node(0, 0)
        node2 = Node(1, 0)
        self.assertEqual(1, Node.distanceBetween(node1, node2))

        node1 = Node(0, 0)
        node2 = Node(1, 1)
        self.assertEqual(math.sqrt(2), Node.distanceBetween(node1, node2))

        node1 = Node(0, 0)
        node2 = Node(0, 2)
        self.assertEqual(2, Node.distanceBetween(node1, node2))

        node1 = Node(-4, 0)
        node2 = Node(8, 12)
        self.assertAlmostEqual(12 * math.sqrt(2), Node.distanceBetween(node1, node2), delta=0.000000000001)

    def test_equals_noLabel(self):
        node1 = Node(0, 3)
        node2 = Node(0, 3)

        self.assertEqual(node1, node2)

    def test_equals_withLabel(self):
        node1 = Node(0, 3, "label")
        node2 = Node(0, 3, "label")

        self.assertEqual(node1, node2)

    def test_not_equals_noLabel(self):
        node1 = Node(0, 2)
        node2 = Node(0, 3)

        self.assertNotEqual(node1, node2)

    def test_not_equals_withLabel(self):
        node1 = Node(0, 3, "a")
        node2 = Node(0, 3, "b")

        self.assertNotEqual(node1, node2)