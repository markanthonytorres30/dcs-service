from sqlalchemy.orm import Session
from sqlalchemy import select, insert


import models


def get_todo_list(db: Session, request):
    result = db.scalars(select(models.Todo).where(models.Todo.deleted == False)).all()
    return result
    