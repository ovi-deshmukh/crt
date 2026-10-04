import unittest
from task import setZeroes

class TestAssignment(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(setZeroes([[1,1,1],[1,0,1],[1,1,1]]),[[1,0,1],[0,0,0],[1,0,1]])

    def test_case2(self):
        self.assertEqual(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]),[[0,0,0,0],[0,4,5,0],[0,3,1,0]])

    
if __name__ == "__main__":
    unittest.main()
