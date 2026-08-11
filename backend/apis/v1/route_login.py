from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from backend.db.session import get_db
from backend.core.config import settings
from backend.core.hashing import Hasher
from backend.db.repository.login import get_user_by_email
from backend.core.security import create_access_token

router = APIRouter()

def authenticate_user(email: str, password: str, db: Session):
    user = get_user_by_email(email=email, db=db)
    if not user:
        return False
    if not Hasher.verify_password(password, user.hashed_password):
        return False
    return user

@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/token")

def get_current_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_email(email=email, db=db)
    if user is None:
        raise credentials_exception
    return user