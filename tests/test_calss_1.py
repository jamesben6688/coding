import unittest
from Google import Demo
# from my_classes.class_1 import Demo


class TestClassDemo(unittest.TestCase):
    def test_add(self):
        cls = Demo()
        res = 0
        self.assertEqual(cls.add(1, -1), res, f"the result should be 0 rather than {res}")

    def test_sub(self):
        cls = Demo()
        res = 1
        self.assertEqual(cls.sub(0, 1), res, f"the result should be -1 rather than {res}")