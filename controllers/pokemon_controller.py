from fastapi import APIRouter, HTTPException
from models import pokemon 
from services import pokemon_service

router = APIRouter(
    prefix="/pokemons",
    tags=["Pokemons"]
)

@router.get("/{id}")
async def get_by_id(id: int | str):
  pokemon = await pokemon_service.get_by_id(id)
  
  if pokemon is None:
    raise HTTPException(status_code=404, detail="Pokemon not found")
  
  return pokemon
