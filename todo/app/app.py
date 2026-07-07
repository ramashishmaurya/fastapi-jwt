from fastapi import FastAPI, Request  , Depends
from typing import Annotated
from app.routing import todos

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.config.app_config import getappconfig

import os 
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()



# include all routes here 
# customize rthe exception right that other can understand 
app.include_router(todos.router)

@app.exception_handler(RequestValidationError) # 
async def validation_exception_handler(request : Request, exe : RequestValidationError):
    print(f"the error is {exe}")
    errors = {}

    for error in exe.errors():
        field = error["loc"][-1]
        message = error["msg"]
        errors[field] = message
    
    return JSONResponse(
        status_code=400 , 
        content={
            "messages":"validation error" , 
            "error":errors
        } 
    )




# @app.get('/')
# def getroutes(query : Annotated[Usermodel , Depends()]):
#     return {
#         'params' : query
#     }

@app.get('/ashish/{user_id}') 
def func(user_id):

    return {'message': f" this is user id {user_id} from reguests data okay "}

@app.get('/')
def getdata():
    config = getappconfig()
    return({
        "app_name" : config.app_name , 
        "app_env" : config.app_env 
    })