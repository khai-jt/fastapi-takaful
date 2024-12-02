from fastapi import FastAPI

from controllers import pokemon_controller

app = FastAPI()

app.include_router(pokemon_controller.router)

