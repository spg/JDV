from networkx.algorithms.shortest_paths.generic import shortest_path
from src.robot.ai.graph.node import Node
import networkx as nx

class SimpleGraph:
    def __init__(self):
        self.g = nx.Graph()

    def add_edge(self, node1, node2):
        if not isinstance(node1, Node) or not isinstance(node2, Node):
            raise TypeError
        self.g.add_edge(node1, node2, distance=Node.distanceBetween(node1, node2))

    def shortest_path(self, depart, arrivee):
        return shortest_path(self.g, depart, arrivee, "distance")

