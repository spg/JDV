import unittest
from src.robot.ai.singleton import Singleton
from src.robot.ai.singletonaccessexception import SingletonAccessException

class TestSingleton(unittest.TestCase):
    def setUp(self):
        Singleton.instance = None

    def test_instanceIsNotNone(self):
        singleton = Singleton()

        self.assertIsNotNone(singleton.instance)

    def test_constructorThrows(self):
        Singleton()

        self.assertRaises(SingletonAccessException, Singleton)