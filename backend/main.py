from fastapi import FastAPI
from backend.core.config import settings
from backend.db.session import engine
from backend.db.base_class import Base

def create_tables():
    if not engine:
        print("Database engine is not available; skipping table creation.")
        return

    try:
        Base.metadata.create_all(bind=engine)
    except Exception as exc:
        print(f"Warning: could not create tables: {exc}")

def start_application():
    create_tables()
    return FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app = start_application()

@app.get("/")
async def root():
    return {"message": "Hello World"}