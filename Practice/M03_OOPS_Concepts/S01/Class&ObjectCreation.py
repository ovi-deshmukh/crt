'''
OOPs -->Object - Oriented Programming System

Class -->Blueprint / Template
         --> Attributes/ Properties
         --> Methods
Syntax:
class C2:
    pass
C2 --> class
It is a simple Bluprint

Object --->Instance Of Class
a = C2()

a --> object
'''
class Student:
    pass
s1 = Student()
s2 = Student()
s3 = Student()

s1.name = 'Ram'
s2.name = 'Kalyani'
s3.name = 'Vardhan'
print(s1.name)
print(s2.name)
print(s3.name)

'''
#Can we create no.of objects with the same class or not? Yes
#Purpose of OOPs:
1. Code Resuability
2. Security
3. Easy to maintain
4. Code Extend

#Types of Variables:
3 Types
1. Instance Variables  --> Variables (Inside the Objects)
2. Local Variables --> Variables (Inside the Method)
3. Class Variables --> Variables (Inside the Class)
'''
class Employee:
    x = "Sai"   #-->Class Var
    def display(name):
        name = "Saranya"    #Local Var
        print(name)
emp1 = Employee()
emp1.name ="Krishna"      #Instance Var
print(emp1.x)
print(emp1.name)
emp1.display()