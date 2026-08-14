from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.schemas.user import UserCreate, ShowUser
from backend.db.session import get_db
from backend.db.repository.user import create_new_user
from backend.core.permission import require_roles
from backend.db.models.user import User


router = APIRouter()

@router.post("/", response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db), admin_user: User = Depends(require_roles("Superadmin"))):
    return create_new_user(user=user, db=db)
