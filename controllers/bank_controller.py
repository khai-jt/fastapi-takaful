from fastapi import APIRouter
from models import bank
from services import bank_service

router = APIRouter(
    prefix="/bank",
    tags=["Bank"]
)

@router.post("/account/create")
async def create(fname: str, lname: str, deposit: int) -> bank.BankAccount:
    
    account = await bank_service.create_bank_account(fname, lname, deposit)

    return account