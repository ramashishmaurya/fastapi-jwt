from pydantic import BaseModel
from typing import Optional
class student(BaseModel):
    id : Optional[int] = None
    email : str 
    password : str

