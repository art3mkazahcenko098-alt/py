from sqlalchemy.orm import Session
from app.models.user import User, Role
from app.core.security import hash_password
from app.schemas.user import UserCreate

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int):
    return db.get(User, user_id)

def create_user(db: Session, data: UserCreate) -> User:
    user = User(email=data.email, hashed_password=hash_password(data.password), role=Role.user)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
