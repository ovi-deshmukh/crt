#Task
class Student:
   def __init__(self, name, roll_no, marks):
      self.name = name
      self.roll_no = roll_no
      self.marks = marks

   def display(self):
      print(f"Name: {self.name}")
      print(f"Roll No: {self.roll_no}")
      print(f"Marks: {self.marks}")
   
if __name__ == '__main__':
   name = input()
   roll_no = int(input())
   marks = int(input())

   student = Student(name, roll_no, marks)
   student.display()
