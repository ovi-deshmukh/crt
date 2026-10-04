#Tasks
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll No: {self.roll_no}")
        print(f"Course: {self.course}")

if __name__ == '__main__':
    name = input()
    age = int(input())
    roll_no = int(input())
    course = input()

    student = Student(name, age, roll_no, course)
    student.display()

