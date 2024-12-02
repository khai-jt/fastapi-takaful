from pydantic import BaseModel
from uuid import UUID

# QUESTION 1

class Question1AnswerRequest(BaseModel):
    id: UUID
    answer: list[list[int]]


class Question1AnswerResponse(BaseModel):
    id: UUID
    answer: list[list[int]]
    candidate_answer: list[list[int]]
    result: bool


# QUESTION 2

class Question2AnswerRequest(BaseModel):
    url: str


class Question2AnswerResponse(BaseModel):
    url: str
    id: str
