from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate
from security import hash_password

def create_user(db: Session, user: UserCreate):
    db_user = User(
        name= user.name,
        email=user.email,
        password=hash_password(user.password) 
    ) 

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def getdata(db:Session):
    users = db.query(User).all()
    return users

def updatedata(db:Session , user_id : int , user:UserCreate):
    db_user = db.query(User).filter(User.id ==user_id).first()
    if db_user is None:
        return None
    
    db_user.name = user.name 
    db_user.email = user.email
    db_user.password = user.password

    db.commit()
    db.refresh(db_user)
    return db_user

def getdatabyid(db:Session , user_id :int):
    db_user = db.query(User).filter(User.id ==user_id).first()
    return db_user

def deleteuser(db:Session , user_id :int):
    db_data = db.query(User).filter(User.id ==user_id).first() 
    if db_data is None:
        return {"database":"Ente the correct id to delete right"}
    db.delete(db_data)
    db.commit()
    return db_data

