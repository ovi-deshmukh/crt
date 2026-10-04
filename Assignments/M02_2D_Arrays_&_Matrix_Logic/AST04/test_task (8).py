import unittest
from task import diagonalSort

class TestAssignment(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(diagonalSort([[3, 3, 1, 1],[2, 2, 1, 2],[1, 1, 1, 2]]),[[1, 1, 1, 1],[1, 2, 2, 2],[1, 2, 3, 3]])

    def test_case2(self):
        self.assertEqual(diagonalSort([[8, 4, 1],[4, 4, 1],[4, 4, 2]]),[[2, 1, 1],[4, 4, 4],[4, 4, 8]])

if __name__ == "__main__":
    unittest.main()
