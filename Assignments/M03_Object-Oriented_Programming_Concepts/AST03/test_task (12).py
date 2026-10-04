import unittest
from task import Student

class TestAssignment(unittest.TestCase):

    def test_case1(self):
        student = Student("Rahul", 20, 101, "Python")

        self.assertEqual(student.name, "Rahul")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.roll_no, 101)
        self.assertEqual(student.course, "Python")

    def test_case2(self):
        student = Student("Priya", 21, 102, "Java")

        self.assertEqual(student.name, "Priya")
        self.assertEqual(student.age, 21)
        self.assertEqual(student.roll_no, 102)
        self.assertEqual(student.course, "Java")


if __name__ == "__main__":
    unittest.main()

if __name__ == "__main__":
    unittest.main()
