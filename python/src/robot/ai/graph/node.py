import math

class Node:
    def __init__(self, x, y, label = None):
        self.x = x
        self.y = y
        self.label = label

    def __repr__(self):
        return "< " + str(self.label) + " " + str(self.x) + ", " + str(self.y) + ">"

    def __key(self):
        return self.x, self.y, self.label

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    @staticmethod
    def distanceBetween(node1, node2):
        term1 = math.pow(node2.x - node1.x, 2)
        term2 = math.pow(node2.y - node1.y, 2)

        return math.sqrt(term1 + term2)