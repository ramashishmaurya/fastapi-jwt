from pydantic import BaseModel

class Usermodel(BaseModel):
    name : str 
    age : int 
    location : str 