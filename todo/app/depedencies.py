from fastapi.security import OAuth2PasswordBearer 

from fastapi import Depends , HTTPException , status 
from typing import Annotated

from .helper import DecodeAccessTokes
from jwt.exceptions import InvalidAlgorithmError , InvalidTokenError

auth2_schema = OAuth2PasswordBearer(tokenUrl='api/auth/login')

def authentucate_user(token : Annotated[str , Depends(auth2_schema)]):
    try:
        payload = DecodeAccessTokes(token)
        return payload
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED , 
            detail="could not validate creadantial" , 
            headers={"Authorization":"Bearer"}
        )
