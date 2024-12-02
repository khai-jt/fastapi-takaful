from httpx import AsyncClient
from models import question
from pydantic import ValidationError

API_KEY = ""
ENDPOINT = "https://assessment.takafulbrunei.com/v1/question"
HEADERS = {"x-api-key": API_KEY}

client = AsyncClient()

async def answer_question_one(answer: question.Question1AnswerRequest) -> str:

    response = await client.post(ENDPOINT + "/1", headers=HEADERS, json=answer)

    if response.status_code == 422:
        return "failed"
    
    # Validate the data of the response
    data = response.json()

    try:
        question.Question1AnswerResponse.model_validate(data)
    
    except:
        return "invalid"
    
    else:
        return "success"


async def answer_question_two(answer: question.Question2AnswerRequest) -> str:

    response = await client.post(ENDPOINT + "/2", headers=HEADERS, json=answer)

    if response.status_code == 422:
        return "failed"
    
    # Validate the data of the response
    data = response.json()

    try:
        question.Question2AnswerResponse.model_validate(data)
    
    except ValidationError:
        return "invalid"
    
    except:
        return "failed"
    
    else:
        return "success"