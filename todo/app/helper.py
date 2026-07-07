from passlib.context import CryptContext
import jwt
from app.config.app_config import getappconfig
from datetime import datetime , timedelta , timezone

config = getappconfig()

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def CreateAccessTokens(data:dict , expireinminutes:int =30) -> str:
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=expireinminutes)
    to_encode.update({'exp' : expire})
    encoded_jwt = jwt.encode(to_encode , config.secret_key , algorithm=config.algorithm)

    return encoded_jwt

 
def DecodeAccessTokes(token:str) -> dict:
    payload = jwt.decode(
        token , config.secret_key , config.algorithm
    )

    return payload

