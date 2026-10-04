import math

class Circle:
   def __init__(self, radius):
      self.radius = radius
   def area(self):
      return math.pi * self.radius * self.radius

class Rectangle:
   def __init__(self, length, breadth):
      self.length = length
      self.breadth = breadth
   def area(self):
      return self.length * self.breadth

class Triangle:
   def __init__(self, base, height):
      self.base = base
      self.height = height
   def area(self):
      return 0.5 * self.base * self.height
   
if __name__ == '__main__':
   shape = input()

   if shape == "Circle":
      radius = float(input())
      obj = Circle(radius)

   elif shape == "Rectangle":
      length = float(input())
      breadth = float(input())
      obj = Rectangle(length, breadth)

   else:
      base = float(input())
      height = float(input())
      obj = Triangle(base, height)

   print("Area: {:.2f}".format(obj.area()))
