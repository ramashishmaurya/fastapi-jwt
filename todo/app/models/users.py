from pydantic import BaseModel
from typing import Optional
class student(BaseModel):
    id: int
    name : str
    email : str
    password :Optional[str] = None


class StudentResponse(BaseModel):
    id: int
    name: str
    email: str