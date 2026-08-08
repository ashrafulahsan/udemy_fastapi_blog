from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..core.config import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print(f"SQLALCHEMY_DATABASE_URL: {SQLALCHEMY_DATABASE_URL}")

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
except Exception as exc:
    print(f"Database initialization warning: {exc}")
    engine = None
    SessionLocal = None

