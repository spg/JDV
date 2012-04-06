import unittest

class TestString(unittest.TestCase):
    def test_manchesterCodeAndDistance(self):
        manchesterCodeAndDistance = "1010010-284"

        self.assertEqual("1010010", manchesterCodeAndDistance[0:7])
        self.assertEqual("284", manchesterCodeAndDistance[8:])