import unittest
from task import Student

class TestAssignment(unittest.TestCase):

    def test_case1(self):
        student = Student("Rahul", 101, 85)

        self.assertEqual(student.name, "Rahul")
        self.assertEqual(student.roll_no, 101)
        self.assertEqual(student.marks, 85)

    def test_case2(self):
        student = Student("Priya", 102, 92)

        self.assertEqual(student.name, "Priya")
        self.assertEqual(student.roll_no, 102)
        self.assertEqual(student.marks, 92)


if __name__ == "__main__":
    unittest.main()