'''
Polymorphism :
Poly --> Many
Morphism --> Forms

Polymorphism --> Many Forms
Same Method name can act as differently 

JAVA -->Polymorphism -->Method Overriding and Method Overloading
Python --> Polymorphism --> Method Overriding , Duck Typing

Method Overriding :
Same method name can behave differenlty in different classes

class Vehicle:
    def sound(self):
        print("Vehicle gives Sound")
class Bike:
    def sound(self):
        print("Bike gives Sound")
class Car:
    def sound(self):
        print("Car gives Sound")
        
b = Bike()
b.sound()
c = Car()
c.sound()

for obj in [Bike(),Car()]:
    obj.sound()

#Method Overloading-->Same method name with different Arguments
class Cal:
    def sum1(self,a,b,c):
        print(a+b)
class Circle:
    def sum1(self,r):
        print(2 * 3.14 * r * r)
obj1 = Circle(5)
obj2 = Circle(10)
a = Cal(10,20)
d = Cal(10,20,30)

Duck Typing -->If it is required for an object to use method, it tells us to use the object 
                without the type object

class Dog:
    def sound(self):
        print("Bow-Bow")
class Cat:
    def sound(self):
        print("Meo-Meow")
def make_sound(animal):    #animal-->Object for method make_sound()
    animal.sound()
make_sound(Dog())
make_sound(Cat())'''

#Inheritance:
class Animal:
    def sound(self):
        print("Animal makes Sound")
class Dog(Animal):
    def sound(self):
        print("Bow-Bow")
class Cat(Animal):
    def sound(self):
        print("Meow-Meow")
        super().sound()
for obj in [Dog(),Cat()]:
    obj.sound()