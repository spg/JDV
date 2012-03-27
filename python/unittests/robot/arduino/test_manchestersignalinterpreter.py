import unittest
from python.src.robot.arduino.manchestersignalinterpreter import ManchesterSignalInterpreter

class TestManchesterSignalInterpreter(unittest.TestCase):
    def test_interpretSignal_1(self):
        signal = "011000"

        interpreter = ManchesterSignalInterpreter()

        parameters = interpreter.interpretSignal(signal)

        self.assertEqual(3, len(parameters))
        self.assertEqual(ManchesterSignalInterpreter.FIGURE_3, parameters[0])
        self.assertEqual(ManchesterSignalInterpreter.NORTH, parameters[1])
        self.assertEqual(ManchesterSignalInterpreter.FACTOR_2, parameters[2])

    def test_interpretSignal_2(self):
        signal = "110101"

        interpreter = ManchesterSignalInterpreter()

        parameters = interpreter.interpretSignal(signal)

        self.assertEqual(3, len(parameters))
        self.assertEqual(ManchesterSignalInterpreter.FIGURE_6, parameters[0])
        self.assertEqual(ManchesterSignalInterpreter.SOUTH, parameters[1])
        self.assertEqual(ManchesterSignalInterpreter.FACTOR_4, parameters[2])

    def test_interpretSignal_3(self):
        signal = "000000"

        interpreter = ManchesterSignalInterpreter()

        parameters = interpreter.interpretSignal(signal)

        self.assertEqual(3, len(parameters))
        self.assertEqual(ManchesterSignalInterpreter.FIGURE_0, parameters[0])
        self.assertEqual(ManchesterSignalInterpreter.NORTH, parameters[1])
        self.assertEqual(ManchesterSignalInterpreter.FACTOR_2, parameters[2])