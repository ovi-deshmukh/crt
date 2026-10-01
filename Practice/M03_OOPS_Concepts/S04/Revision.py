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

4 Pillars:
1. Encapsulation
2. Inheritance
3. Abstraction
4. Polymorphism

1. Encapsulation : Bundling of Data and Methods in a single unit / Class.
     Access Modifiers : Access Variables inside the Class
       3 Types
        1. Public --> Anyone access in anywhere
        2. Protected  --> Access in class and a child class (_)
        3. Private --> Access inside the class (__)

2. Inheritance : A class can inherit the properties or behaviours from another class.
    1. Parent class/ Main class/ Super class/ Base Class : 
    2. Child class/ Sub class / Derived Class :

    Types : 
        1. Single
        2. Multi- level
        3. Multiple
        4. Hierarchical
        5. Hybrid
        
3. Abstraction : It hides the internal Implementation ,shows the essential Functions to the user
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

    from abc import ABC as Kalyani, abstractmethod
       # abc --> module
       # ABC --> Abstract Base Class
        
4. Polymorphism :
    Poly --> Many
    Morphism --> Forms

    Polymorphism --> Many Forms
    Same Method name can act as differently 

    JAVA -->Polymorphism -->Method Overriding and Method Overloading
    Python --> Polymorphism --> Method Overriding , Duck Typing

    Method Overriding : Same method name can behave differenlty in different classes
'''