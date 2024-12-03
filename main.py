from fastapi import FastAPI

from controllers import bank_controller

app = FastAPI()

app.include_router(bank_controller.router)

