from fastapi import APIRouter
from models import bank
from services import bank_service

router = APIRouter(
    prefix="/bank",
    tags=["Bank"]
)

@router.get("/account/create")
async def create(fname: str, lname: str, deposit: float):
    
    account = await bank_service.create_bank_account(fname, lname, deposit)

    # print(account)
    # return f"Account created for {account.customer}. Balance is {account.balance}"

    return account