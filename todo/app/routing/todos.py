from fastapi import APIRouter , Depends
from app.models.todos import CreateTodo

router  = APIRouter(prefix='/todo')

@router.get('/')
def index():
    return {'messages':'this is todos api routers '}

@router.post('/')
def postvalues(abc:CreateTodo):
    print(abc)
    return {
        'message':'create new todo okay' , 
        'items' : abc.model_dump()
    }
