import unittest

import unittest
from ant_on_the_boundry import ant_on_the_boundry

class TestAntOnTheBoundary(unittest.TestCase):

    def test_ant_on_the_boundary(self):
        # Test case 1
        list_num_1 = [2, -2, 5, -3, -2, 1]
        self.assertEqual(ant_on_the_boundry(list_num_1), 2)

        # Test case 2
        list_num_2 = [1, -1, 1, -1, 1, -1]
        self.assertEqual(ant_on_the_boundry(list_num_2), 3)

        # Test case 3
        list_num_3 = [1, 1, 1, 1, 1, 1]
        self.assertEqual(ant_on_the_boundry(list_num_3), 0)

        # Test case 4
        list_num_4 = [0, 0, 0, 0, 0, 0]
        self.assertEqual(ant_on_the_boundry(list_num_4), 6)

if __name__ == '__main__':
    unittest.main()

