from pydantic import BaseModel
from datetime import datetime

class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    id: int
    prompt: str
    response: str
    created_at: datetime

    class Config:
        from_attributes = True