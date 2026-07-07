from pydantic import BaseModel , Field , StrictStr
from typing import Optional , Annotated
from typing import Optional


class CreateTodo(BaseModel):
    content : Annotated[str, Field(max_length=30 , min_length=4)]
    is_completed : Optional[bool] = None
    

