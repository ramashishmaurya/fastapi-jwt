from fastapi import APIRouter , Depends 
from app.models.users import student , StudentResponse

from app.database.db import get_db
from typing import Annotated 
from app.schema.user_schema import UserSchema
from app.helper import hash_password
from sqlalchemy.orm import Session

router = APIRouter(prefix="/user")


@router.get("/")
def getinfo(db:Annotated[Session , Depends(get_db)]):
    user = db.query(UserSchema).all()
    return user


@router.post("/")
def store(items :student , db:Annotated[Session , Depends(get_db)]):
    user = UserSchema(name = items.name , email =items.email , password = hash_password(items.password ))
    db.add(user)
    db.commit()
    db.refresh(user)

    return ({"messages":"Created new toddo" , "items" : user})

@router.get("/{user_id}")
def sdetail(user_id :int , db : Annotated[Session , Depends(get_db)]):
    todo = db.query(UserSchema).filter(UserSchema.id ==user_id).first()
    return({
        "getting the data by id " : todo
    })


@router.put("/{user_id}")
def updatdata(user_id : int , db : Annotated[Session , Depends(get_db)] , items : student):
    todo = db.query(UserSchema).filter(UserSchema.id == user_id).first()
    if todo is None:
        return({'message' : f'this {todo} is not available right'})
    todo.email = items.email
    todo.password = items.password

    db.commit()
    db.refresh(todo)
    return({'message' : todo})

@router.delete("/{user_id}")
def deleteuser(user_id : int , db:Annotated[Session , Depends(get_db)]):
    todo = db.query(UserSchema).filter(UserSchema.id ==user_id ).first()
    if todo is None:
        return({'error' : f'this name {todo} is not avai;able right'})
    db.delete(todo)
    db.commit()
    return({'messages' : f"this {user_id} is deleetd suceessfully"})


@router.get('/ashish')
def get_user(
    skip: int = 0,
    limit: int = 2,
    db: Session = Depends(get_db) 
):
    user = (
        db.query(UserSchema)
        .offset(skip)
        .limit(limit)
        .all()
    )

    return user


