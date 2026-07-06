from pydantic import BaseModel , Field , StrictStr
from typing import Optional , Annotated


class CreateTodo(BaseModel):
    content : Annotated[StrictStr , Field(max_length=10 , min_length=4)]
    is_completed : bool = False
    

