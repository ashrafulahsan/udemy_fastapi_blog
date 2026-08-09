from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db.session import get_db
from backend.schemas.blog import CreateBlog, ShowBlog
from backend.db.repository.blog import create_new_blog, retrive_blog


router = APIRouter()

@router.post("/", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    return create_new_blog(blog=blog, db=db, user_id=1)  # Replace with actual user ID in a real application

@router.get("/{id}", response_model=ShowBlog, status_code=status.HTTP_200_OK)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = retrive_blog(id=id, db=db)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    return blog