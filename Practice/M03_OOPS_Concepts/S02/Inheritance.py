'''
Inheritance : A class can inherit the properties or behaviours from another class.
1. Parent class/ Main class/ Super class/ Base Class : 
2. Child class/ Sub class / Derived Class :

Types : 
1. Single
2. Multi- level
3. Multiple
4. Hierarchical
5. Hybrid

1. Single Inheritance: One Parent class and One Child class
Syntax:
class Parent:
     |
     |
class Child(Parent):
'''
class A:     #Parent
    def display(self):
        print("This is a Parent Class")
class B(A):    #Child
    def display2(self):
        print("This is a child class")
b = B()
b.display2()
'''
#2. Multi-Level Inheritance: 
Syntax:
Grand Parents
  |
  |
Parents
  |
  |
Child
'''
class A:
    def display(self):
        print("This is a GrandParent class")
class B(A):
    def display2(self):
        print("This is a Parent class")
class C(B):
    def display3(self):
        print("This is a Child class")
c = C()
c.display()
c.display2()
c.display3()
'''
3. Hierarchical Inheritance:
Syntax:
One Parent :
     |
     |
Two or more Child classes
'''
class Father:
    def land(self):
        print("Father Property")
class Bro(Father):
    def pro(self):
        print("Bro Property")
class Sis(Father):
    def pro1(self):
        print("Sis Property")
class Bro2(Father):
    def pro3(self):
        print("Bro3 Property")
b = Bro2()
b.pro3()
'''
4. Multiple Inheritance:
Syntax:
One Child classes
    |
    |
Two or more Parent
'''
class Father:
    def Car(self):
        print("Father Car")
class Mother:
    def Car(self):
        print("Mother LAnd")
class child(Father,Mother):
    def study(self):
        print("Studying")
obj = child()
obj.Car()

    