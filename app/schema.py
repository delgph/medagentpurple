from pydantic import BaseModel
from typing import Any, Dict

class Task(BaseModel):
    id: str
    type: str
    payload: Dict[str, Any]

class AgentResponse(BaseModel):
    status: str
    result: Dict[str, Any]
