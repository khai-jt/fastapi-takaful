from pydantic import BaseModel

# Pokemon
class Pokemon(BaseModel):
    id: int
    name: str
    base_experience: int
    

