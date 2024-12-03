from models import bank

async def create_bank_account(fname: str, lname: str, deposit: float):

    customer = bank.Customer(fname, lname)

    bank_account = bank.BankAccount(customer, deposit)

    return { "customer": bank_account.get_customer_full_name(), "balance": bank_account.get_balance() }
