
class Customer:
    def __init__(self, firstname: str, surname: str):
        self.firstname = firstname
        self.surname = surname


class BankAccount:
    def __init__(self, account_holder: Customer, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: int):
        self.balance += amount
        return self.balance

    def withdraw(self, amount: int):
        self.balance += amount
        return self.balance


    def get_balance(self, amount: int):
        return self.balance



class CheckingAccount(BankAccount):
    def __init__(self, account_holder: Customer, balance: float):
        super().__init__(account_holder, balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_holder: Customer, balance: float):
        super().__init__(account_holder, balance)

