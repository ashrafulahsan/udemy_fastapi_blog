from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db.session import get_db
from backend.schemas.blog import CreateBlog, ShowBlog
from backend.db.repository.blog import create_new_blog, retrive_blog, list_blogs, update_blog_by_id


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

@router.get("/", response_model=list[ShowBlog], status_code=status.HTTP_200_OK)
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return blogs

@router.put("/{id}", response_model=ShowBlog, status_code=status.HTTP_200_OK)
def update_blog(id: int, blog: CreateBlog, db: Session = Depends(get_db)):
    blog = update_blog_by_id(id=id, blog=blog, db=db, user_id=1)  # Replace with actual user ID in a real application
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    return blog