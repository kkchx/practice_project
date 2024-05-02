import unittest
from apples import minimumBoxes


class TestMinimumBoxes(unittest.TestCase):
    def test1(self):
        self.assertEqual(minimumBoxes([1,3,2],[4,3,1,5,2]),2)  # add assertion here
    def test2(self):
        self.assertEqual(minimumBoxes([5,5,5],[2,4,2,7]), 4)

    def test3(self):
        self.assertEqual(minimumBoxes([9,8,8,2,3,1,6], [10,1,4,10,8,5]), 5)

if __name__ == '__main__':
    unittest.main()
