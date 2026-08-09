from sqlalchemy.orm import Session
from backend.schemas.blog import CreateBlog
from backend.db.models.blog import Blog

def create_new_blog(blog: CreateBlog, db: Session, user_id: int = 1):
    new_blog = Blog(
        title=blog.title, 
        slug=blog.slug,
        content=blog.content, 
        user_id=user_id
        )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def retrive_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog