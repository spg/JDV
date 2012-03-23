import unittest
from python.src.robot.ai.states.advancestate import AdvanceState
from python.src.robot.ai.statecontroller import StateController

class TestStateController(unittest.TestCase):
    def setUp(self):
        pass

    def test_mainloop(self):
        stateController = StateController(AdvanceState())
        stateController.beginMainLopp()
