from fastapi import APIRouter , Depends
from app.models.todos import CreateTodo
from app.database.db import get_db 
from sqlalchemy.orm import Session
from typing import Annotated
from app.models.todos import CreateTodo
from app.schema.todo_schema import  TodoSchema
router  = APIRouter(prefix='/todo')

@router.get("/")
def index(db:Annotated[Session , Depends(get_db)]):
    todo = db.query(TodoSchema).all()
    return({
        "all data" : todo
    })

@router.post("/")
def store(items :CreateTodo , db:Annotated[Session , Depends(get_db)]):
    todo = TodoSchema(content = items.content)
    db.add(todo)
    db.commit()
    db.refresh(todo)

    return ({"messages":"Created new toddo" , "items" : todo})

@router.get("/{user_id}")
def sdetail(user_id :int , db : Annotated[Session , Depends(get_db)]):
    todo = db.query(TodoSchema).filter(TodoSchema.id ==user_id).first()
    return({
        "getting the data by id " : todo
    })

@router.put("/{user_id}")
def updatdata(user_id : int , db : Annotated[Session , Depends(get_db)] , items : CreateTodo):
    todo = db.query(TodoSchema).filter(TodoSchema.id == user_id).first()
    if todo is None:
        return({'message' : f'this {todo} is not available right'})
    todo.content = items.content

    db.commit()
    db.refresh(todo)
    return({'message' : 'ashosh'})

@router.delete("/{user_id}")
def deleteuser(user_id : int , db:Annotated[Session , Depends(get_db)]):
    todo = db.query(TodoSchema).filter(TodoSchema.id ==user_id ).first()
    if todo is None:
        return({'error' : f'this name {todo} is not avai;able right'})
    db.delete(todo)
    db.commit()
    return({'messages' : f"this {user_id} is deleetd suceessfully"})