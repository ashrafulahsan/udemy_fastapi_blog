from fastapi import FastAPI
from backend.core.config import settings
from backend.db.session import engine
from backend.db.base import Base

def create_tables():
    if not engine:
        raise RuntimeError("Database engine is not available.")

    Base.metadata.create_all(bind=engine)

def start_application():
    create_tables()
    return FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app = start_application()

@app.get("/")
async def root():
    return {"message": "Hello World"}