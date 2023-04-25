import os
import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import registry

host = os.getenv("DB_HOST", "localhost")
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://root:1qazxsw2@{host}/dcsone_1?charset=utf8mb4"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

try:
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )
except Exception as e:
    print("MYSQL not responds.. waiting for mysql up: %s" % e)
    time.sleep(1)
finally:
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    reg = registry()
    pass