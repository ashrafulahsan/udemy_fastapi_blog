from sqlalchemy.orm import Session
from backend.schemas.user import UserCreate
from backend.db.models.user import User
from backend.core.hashing import Hasher

def create_new_user(user: UserCreate, db: Session) -> User:
    db_user = User(
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        is_active=True
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user