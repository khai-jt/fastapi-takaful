from pydantic import BaseModel, EmailStr


# CANDIDATE

class CandidateRegisterResponse(BaseModel):
    name: str
    api_key: str


class CandidateRegistrationRequest(BaseModel):
    email_address: EmailStr
    name: str

