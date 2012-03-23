import unittest
from mock import MagicMock
import serial

class TestMotorControls(unittest.TestCase):
    def test_advance(self):
        maison = Maison()
        maison.getNbPortes = MagicMock(return_value = 3)

        print maison.getNbPortes()

        mySerial = serial.Serial()
        mySerial.read = MagicMock(return_value = 10)

        print mySerial.read()

class Maison:
    def __init__(self):
        self.nbPortes = 4

    def getNbPortes(self):
        return self.nbPortes

