from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.apis.v1.route_login import get_current_user
from backend.db.models.user import User
from backend.db.session import get_db
from backend.schemas.blog import CreateBlog, ShowBlog
from backend.db.repository.blog import create_new_blog, retrive_blog, list_blogs, update_blog_by_id, delete_blog_by_id


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
def update_blog(id: int, blog: CreateBlog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):  # Replace with actual user ID in a real application
    updated_blog = update_blog_by_id(id=id, blog=blog, db=db, user_id=current_user.id)  # Replace with actual user ID in a real application
    if isinstance(updated_blog, dict):
        raise HTTPException(
            detail=updated_blog.get("error"),
            status_code=status.HTTP_404_NOT_FOUND
        )
    return updated_blog

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_blog(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = delete_blog_by_id(id=id, db=db, user_id=current_user.id)  # Replace with actual user ID in a real application
    if result.get("error"):
        raise HTTPException(
            detail=result.get("error"),
            status_code=status.HTTP_404_NOT_FOUND
        )
    return {"msg": result.get("detail")}