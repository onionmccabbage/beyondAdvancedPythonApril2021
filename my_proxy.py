import random
from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass

class Bank(Payment): 
    def __init__(self):
        self.card = None
        self.account = None   
    def __getAccount(self):
        self.account = self.card # Assume card number is account number
        return self.account    
    def __hasFunds(self):
        print("Bank:: Checking if Account", self.__getAccount(), "has enough funds")
        return bool(random.getrandbits(1)) # fast way to return boolean    
    def setCard(self, card):
        self.card = card    
    def do_pay(self):
        if self.__hasFunds():
            print("Bank:: Paying the merchant")
            return True
        else:
            print("Bank:: Sorry, not enough funds!")
            return False

class DebitCard(Payment): # this is the proxy   
    def __init__(self):
        self.bank = Bank()    
    def do_pay(self):
        card = input("Proxy:: Swipe Card or Phone")
        self.bank.setCard(card)
        return self.bank.do_pay()

class You: 
    def __init__(self):
        print("You:: I'll have a fruity flat iced chai salted spice with whipped cream")
        self.debitCard = DebitCard()
        self.isPurchased = None    
    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()   
    def __del__(self):
        if self.isPurchased:
            print("You:: mmmmmm yummie :-)")
        else:
            print("You:: can you lend me a fiver :(")

if __name__ == '__main__':
    you = You()
    you.make_payment()