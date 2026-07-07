from sqlalchemy import Column , String , Integer , VARCHAR , Boolean , DateTime

from sqlalchemy.orm import Mapped , mapped_column

from app.database.db import Base

from datetime import datetime , timezone , timedelta
class UserSchema(Base):
    __tablename__ = "students"
    id : Mapped[int] = mapped_column(Integer , primary_key=True , index=True , autoincrement=True)
    email : Mapped[str] = mapped_column(String , unique = True , nullable= False)
    password:Mapped[str] = mapped_column(String , nullable=False)
    is_active:Mapped[bool] = mapped_column(Boolean , nullable=False , default=True)
    created_at : Mapped[datetime] =mapped_column(DateTime  , nullable=False , default=datetime.now(timezone.utc))
    updated_at : Mapped[datetime | None] =mapped_column(DateTime  , nullable=False , default=datetime.now(timezone.utc))