from fastapi import Depends
from sqlalchemy.orm import Session

from .crypt import get_hashed_password
from database import get_db
from models import User


def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    hashed_password = get_hashed_password(password)
    user = User(email=email, username=username, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user