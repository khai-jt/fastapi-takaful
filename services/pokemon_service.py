from httpx import AsyncClient
from models import pokemon

API_KEY = ""
ENDPOINT = "https://pokeapi.co/api/v2/pokemon"
HEADERS = {"x-api-key": API_KEY}

client = AsyncClient()

async def get_by_id(id: int | str) -> pokemon.Pokemon | None:

    
    response = await client.get(ENDPOINT + f"/{id}", headers=HEADERS)
    
    if response.status_code == 404:
        return None
    
    # Convert and validate the data of the response
    data = response.json()
    
    x = pokemon.Pokemon(**data)
    return x
   








 