from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.crud.user import create_user
from app.schemas.user import UserCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/")
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)