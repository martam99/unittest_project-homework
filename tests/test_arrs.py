import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 0, "test"), 1)
        self.assertEqual(arrs.get([], 7, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, "Thereisnothing"), 6)
        self.assertEqual(arrs.get([1, 2, 3, 4, 5], 87, "test"), 'test')
        self.assertEqual(arrs.get([1, 2, 3, 4, 5, 6, 7, 8, 9], -5, "Thereisnothing"), 'Thereisnothing')

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5, 6, 7], -1), [7])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5, 6, 7], 0), [1, 2, 3, 4, 5, 6, 7])
