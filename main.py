from fastapi import FastAPI

from controllers import questions_controller

app = FastAPI()

app.include_router(questions_controller.router)

