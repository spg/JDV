import unittest
from src.robot.ai.advancestate import AdvanceState
from src.robot.ai.statecontroller import StateController

class TestStateController(unittest.TestCase):
    def setUp(self):
        pass

    def test_mainloop(self):
        stateController = StateController(AdvanceState())
        stateController.beginMainLopp()
