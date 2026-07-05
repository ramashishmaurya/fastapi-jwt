from sqlalchemy import Column , String , Integer 

from database import Base
from security import hash_password

class User(Base):
     __tablename__ = "users"

     id = Column(Integer , primary_key = True , index  = True)
     name = Column(String)
     email = Column(String , unique=True)
     password = Column(String)

