from pydantic import BaseModel

class SupportRequest(BaseModel):
    query: str

class SupportResponse(BaseModel):
    intent: str
    response: str