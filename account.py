import datetime
import pytz

class InvalidWithdrowal(Exception):
    pass

class Account:
    """"" This is a simple account class
    Args needed to initiate the account
    name: name of the account holder
    amount: Amount to be deposited
    """""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, amount):
        self._accnt_holder = name
        self.__balance = amount
        self.transactionList = [(Account._current_time(), amount, self.__balance)]
        print("The account have been started \nName: {}\nDeposit: {}".format(self._accnt_holder, self.__balance))

    def deposit(self, amount):
        """
        This function in class account is meant for deposit
        Args:
            amount: Amount to be diposited

        Returns: nothing

        """
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self.transactionList.append((Account._current_time(), amount, self.__balance))

    def withdraw(self, amount):
        """
        This function will subtract the withdrawel amount
        Args:
            amount: the amount to be withdrawn

        Returns: nothing

        """
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.show_balance()
            self.transactionList.append((Account._current_time(), -amount, self.__balance))
        else:
            raise InvalidWithdrowal("You dont have that much money")
            # print("Sorry you don't have that much amount")
            self.show_balance()

    def show_balance(self):
        """
        This function print the account balance
        Returns:Nothing

        """
        print("The balance is {}".format(self.__balance))

    def transaction_history(self):
        """
        This function will print the transaction history
        Returns: nothing

        """
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
    Div.withdraw(30000)
    Div.show_balance()
    Div.transaction_history()
    Div.show_balance()
    print()
    print("***************************")
    print()
    jb = Account("Jeya Balaganesh", 0)
    jb.deposit(5000)
    jb.withdraw(500)
    jb.transaction_history()
    # print(Div.__dict__)
    jb.__balance = 10
    jb.show_balance()
    # print(jb.__dict__)
    # help(Account)
    print(jb.deposit.__doc__)
