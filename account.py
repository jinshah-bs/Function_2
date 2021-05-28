import datetime
import pytz


class Account:
    """ This is a simple account class"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, amount):
        self.accntHolder = name
        self.balance = amount
        self.transactionList = [(Account._current_time(), amount, self.balance)]
        print("The account have been started \nName: {}\nDeposit: {}".format(self.accntHolder, self.balance))

    def deposit(self, amount):
        """ This function in class account is meant for deposit"""
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transactionList.append((Account._current_time(), amount, self.balance))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.show_balance()
            self.transactionList.append((Account._current_time(), -amount, self.balance))
        else:
            print("Sorry you don't have that much amount")
            self.show_balance()

    def show_balance(self):
        print("The balance is {}".format(self.balance))

    def transaction_history(self):
        for date, amount, balance in self.transactionList:
            if amount > 0:
                tran_type = "Deposited"
            else:
                tran_type = "Withdrawn"
                amount = -amount
            print("{}, {}, {} and you have {}".format(date.astimezone(), tran_type, amount, balance))


if __name__ == '__main__':
    Div = Account('Divakar', 1000)
    Div.deposit(2000)
    Div.deposit(2000)
    Div.withdraw(1500)
    Div.deposit(1000000)
    Div.withdraw(3000)
    # Divakar.show_balance()
    # Div.transaction_history()
    # Div.show_balance()
    # print()
    # print("***************************")
    # print()
    # jb = Account("Jeya Balaganesh", 0)
    # jb.deposit(5000)
    # jb.withdraw(500)
    # jb.transaction_history()
