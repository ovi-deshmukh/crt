'''
Abstraction : It hides the internal Implementation ,shows the essential Functions to the user

Ex :
External :

ATM
 |
Card
 |
Enter PIN 
  |
withdraw
  |
Cash Draw

Internal :
1. Bank Details
2. Communication between ATM and Bank Server
3. PIN Hides 

#Implement Abstraction in Python:
1. Python Provides a module called --> abc
2. with abc module --> Abstract classes
Abstract Class : Abstract classes are the class created by abc module 
It contains of Abstrcat method
3. Abstract Method : Implementation which is hide is done in abstract method

'''
from abc import ABC as Kalyani, abstractmethod

# abc --> module
# ABC --> Abstract Base Class
class Vehicle(Kalyani):
    @abstractmethod    #Decorator
    def sound(self):
        print("Vehicle gives sound") 
class Car(Vehicle):
    def sound(self):
        print("Car make sound")
v = Vehicle()
v.sound()
c = Car()
c.sound()

#Write a python code using Abstraction for a Payment (UPI & Paytm)?
from abc import ABC as kalyani, abstractmethod
class Payment(kalyani):
    @abstractmethod
    def Trans(self,amount):
        Pass 
class UPI(Payment):
    def Trans(self,amount):
        print("Trans of Ruppes",amount ,"Throught UPI")
class Paytm(Payment):
    def Trans(self,amount):
        print("Trans of Ruppes",amount ,"Throught Paytm")
u =UPI()
u.Trans(500)
p = Paytm()
p.Trans(1000)