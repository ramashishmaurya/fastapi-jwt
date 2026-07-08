import time
from fastapi import FastAPI, Request  , Depends 
from fastapi import Request
from typing import Annotated
from app.routing import todos , users ,auth
import json
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.config.app_config import getappconfig

import os 
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
@app.middleware("http")
async def user_detail(request: Request, call_next):

    print("PATH:", request.url.path)
    print("METHOD:", request.method)

    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    print("TIME:", process_time)

    return response


# include all routes here 
# customize rthe exception right that other can understand 
app.include_router(todos.router , prefix="/api")

app.include_router(users.router ,prefix="/api" )
app.include_router(auth.router , prefix="/api")

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


