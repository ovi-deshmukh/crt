'''
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
'''
class A:
    name = "Kalyani"
    _name = "Ram"
    __name = "Sai"
    # def display1(self):
        # self.__name = name
a = A()
print(a.name)
print(a._name)
print(a._A__name)   
#a.display1()
'''
User --> ATM --> Machine --> data(Account, Balance, Amount)
Hide --> Data of Bank's --> Methods-->{deposit(), withdraw(), Check_balance()} 
'''
#Write a Prgoram using Private variable of a BankAccount()
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        if  self.__balance > 0:
            self.__balance += amount
    def display2(self):
        print(self.__balance)
bank = BankAccount(1000)
bank.deposit(500)
bank.display2()