#Task
class BankAccount:
   def __init__(self, balance):
      self.__balance = balance

   def deposit(self, amount):
      self.__balance += amount

   def withdraw(self, amount):
      if amount > self.__balance:
         return False
      self.__balance -= amount
      return True

   def get_balance(self):
      return self.__balance

if __name__ == '__main__':
   balance = int(input())
   deposit_amount = int(input())
   withdraw_amount = int(input())

   account = BankAccount(balance)

   account.deposit(deposit_amount)

   if not account.withdraw(withdraw_amount):
      print("Insufficient Balance")

   print("Balance:", account.get_balance())
