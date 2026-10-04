import unittest
from task import diagonalBoundarySum

class TestAssignment(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(diagonalBoundarySum([[ 1, 2, 3, 4 ],[ 1, 2, 3, 4 ],[ 1, 2, 3, 4 ],[ 1, 2, 3, 4 ]]),40)

    def test_case2(self):
        self.assertEqual(diagonalBoundarySum([[ 1, 2, 3],[ 1, 2, 3],[ 1, 2, 3]]),18)

if __name__ == "__main__":
    unittest.main()
