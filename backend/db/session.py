from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
try:
    from backend.core.config import settings
except ModuleNotFoundError:
    from core.config import settings
from typing import Generator

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print(f"SQLALCHEMY_DATABASE_URL: {SQLALCHEMY_DATABASE_URL}")

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
except Exception as exc:
    print(f"Database initialization warning: {exc}")
    engine = None
    SessionLocal = None


def get_db() -> Generator:
    if SessionLocal is None:
        raise RuntimeError("Database session is not initialized.")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()