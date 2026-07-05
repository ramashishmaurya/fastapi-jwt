from fastapi import FastAPI , Depends
from sqlalchemy.orm import Session

from database import SessionLocal , engine  , Base
from models  import User 
from schemas import UserCreate 
from crud import create_user , getdata , updatedata , getdatabyid , deleteuser

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()


@app.post("/users")
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@app.get('/users/')
def read_users(db:Session = Depends(get_db)):
    return getdata(db)

@app.put('/updatedata/{user_id}')
def update(user_id : int , user : UserCreate , db:Session = Depends(get_db)):
    update_user = updatedata(db , user_id , user)

    return update_user

@app.get('/getdatabyid/{user_id}')
def getdatar(user_id : int , db: Session = Depends(get_db)):
    return getdatabyid(db , user_id)

@app.delete('/deletedata/{user_id}')
def deleteusers(user_id : int  , db : Session = Depends(get_db)):
    return deleteuser(db , user_id)





