from pydantic import BaseModel

# HTTP Validation Error

class Item(BaseModel):
    loc: list[str | int]
    msg: str
    type: str

class HTTPValidationError(BaseModel):
    detail: list[Item]


# Validation Error

class ValidationError(BaseModel):
    loc: list[str | int]
    msg: str
    type: str

