import unittest
from task import diagonalDifference

class TestAssignment(unittest.TestCase):

    def test1(self):
        self.assertEqual(diagonalDifference([[1,2,3],[4,5,6],[9,8,9]]),2)

    def test2(self):
        self.assertEqual(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]),15)

    def test3(self):
        self.assertEqual(diagonalDifference([[1,1],[1,1]]),0)

if __name__ == "__main__":
    unittest.main()
