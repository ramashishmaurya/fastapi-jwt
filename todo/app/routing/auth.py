from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi.responses import JSONResponse
from app.database.db import get_db
from app.models.auth import Login , Register
from app.schema.user_schema import UserSchema
from app.helper import hash_password , verify_password , CreateAccessTokens , DecodeAccessTokes

router = APIRouter(prefix="/auth")


@router.post('/login')
def login(data:Login , db:Annotated[Session , Depends(get_db)]):
    user = db.query(UserSchema).filter(UserSchema.email == data.email).first()
    if not user or not verify_password(data.password, user.password):
        return JSONResponse(
           status_code=401,
            content={
            "message": "Email or password is incorrect"
        }
    )
    
    payload ={
        "id":user.id , 
        "name":user.name , 
        "email":user.email 

    }

    token = CreateAccessTokens(payload) 
    payload["access_token"] = "Bearer  " + token

    return({'message':"Login successfully" , "data":payload})



@router.post("/register")
def register(data:Register , db:Annotated[Session , Depends(get_db)]):
    existing_user = db.query(UserSchema).filter(UserSchema.email ==data.email).first()
    if existing_user:
        return({'messaged':'USer with this emaail id is already registered'})
    new_user =UserSchema(
        name = data.name , 
        email = data.email , 
        password = hash_password(data.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return({
        'messages' :new_user
    })

