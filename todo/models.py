from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, registry
import datetime

from typing import Optional

from database import Base
  

class Todo(Base):
    __tablename__ = "todo"

    id:Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    task:Mapped[Optional[str]] = mapped_column(String(100),nullable=False)
    done:Mapped[bool] = mapped_column(Boolean,nullable=False)
    deleted:Mapped[bool] = mapped_column(Boolean,nullable=False)
    date_created:Mapped[datetime.datetime] = mapped_column(DateTime,nullable=False,server_default=func.CURRENT_TIMESTAMP())
    date_updated:Mapped[datetime.datetime] = mapped_column(DateTime,nullable=True,onupdate=func.CURRENT_TIMESTAMP())
    

