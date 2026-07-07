from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base
from dotenv import load_dotenv
Base = declarative_base()

from sqlalchemy  import create_engine 
from app.config.app_config import getappconfig

config = getappconfig()

engine = create_engine(config.database_url)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()



