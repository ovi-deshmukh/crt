'''
__init__(): It is a special kind of a method acts like a constructor.
No need to create Object

Syntax: 
class Student:
    def __init__():
        pass
self : It is a keyword -->Represent the current Objects
Syntax:
class Student:
    def __init__(self,name):
        self.name = name
s1 = Student()
s1.name = 'kalyani'
s2 = Student()
s2.name = 'Ram'

self --> s1
self --> s2

#JAVA--> Student s1 = new Student()

def add(a,b):
    return a + b 
res = add(10,20)
print(res)

class Addition:
    def add(self,a,b):
        return a + b 
a = Addition()
print(a.add(10,20))
'''
#Write a program to count how many objects are created to a class?
class Student:
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count += 1
s1 = Student('Ravi')
s2 = Student('Ram')
s3 = Student('Sai')
s4 = Student('Ramesh')
s5 = Student('Rahul')
print(Student.count)

# Leet Code : 1603
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        '''self.big = big
        self.medium = medium
        self.small = small  '''
        self.spaces = [0,big,medium,small]      

    def addCar(self, carType: int) -> bool:
        if self.spaces[carType] >=1:
            self.spaces[carType] -= 1
            return True
        return False
        '''if carType == 1:
            if self.big >= 1:
                self.big -= 1
                return True
        if carType == 2:
            if self.medium >= 1:
                self.medium -= 1
                return True
        if carType == 3:
            if self.small >= 1:
                self.small -= 1
                return True
        return False'''
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)