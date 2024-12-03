from models import bank

async def create_bank_account(fname: str, lname: str, deposit: float) -> bank.BankAccount:

    customer = bank.Customer(fname, lname)

    bank_account = bank.BankAccount(customer, deposit)

    return bank_account
