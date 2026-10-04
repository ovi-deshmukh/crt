from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print("Payment of", amount, "successful using UPI")

class CreditCard(Payment):
    def pay(self, amount):
        print("Payment of", amount, "successful using Credit Card")

class Cash(Payment):
    def pay(self, amount):
        print("Payment of", amount, "successful using Cash")

if __name__ == '__main__':
    payment_type = input()
    amount = int(input())

    if payment_type == "UPI":
        payment = UPI()

    elif payment_type == "CreditCard":
        payment = CreditCard()

    else:
        payment = Cash()

    payment.pay(amount)
