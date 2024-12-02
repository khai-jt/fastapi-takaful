from fastapi import APIRouter
from models import question
from services import question_service

router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)

@router.post("/question/1")
async def answer_question_one(answer: question.Question1AnswerRequest) -> bool:
  result = await question_service.answer_question_one(answer)

  if result == "failed" or result == "invalid":
    return False
  
  return True


@router.post("/question/2")
async def answer_question_two(answer: question.Question2AnswerRequest) -> bool:
  result = await question_service.answer_question_two(answer)

  if (result == "failed" or result == "invalid"):
    return False
  
  return True