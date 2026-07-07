from pydantic import BaseModel  , Field , EmailStr , field_validator , ValidationInfo

class Login(BaseModel):
    email : EmailStr
    password : str = Field(... , min_length= 4 , max_length=40)

from pydantic import BaseModel, EmailStr, model_validator

class Register(BaseModel):
    name:str
    email: EmailStr
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def password_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self
    

from  typing  import Annotated
class Authuser(BaseModel):
    id :Annotated[int , Field(max_length=12 , min_length=12)]
    name:str 
    email :str

