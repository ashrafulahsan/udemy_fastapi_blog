from sqlalchemy.orm import Session
from backend.schemas.blog import CreateBlog, UpdateBlog
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

def list_blogs(db: Session):
    blogs = db.query(Blog).filter(Blog.published == True).all()
    return blogs

def update_blog_by_id(id: int, blog: UpdateBlog, db: Session, user_id: int = 1):
    existing_blog = db.query(Blog).filter(Blog.id == id, Blog.user_id == user_id).first()
    if not existing_blog:
        return None

    existing_blog.title = blog.title
    existing_blog.slug = blog.slug
    existing_blog.content = blog.content
    existing_blog.published = blog.published

    db.commit()
    db.refresh(existing_blog)
    return existing_blog

def delete_blog_by_id(id: int, db: Session, user_id: int = 1):
    existing_blog = db.query(Blog).filter(Blog.id == id, Blog.user_id == user_id).first()
    if not existing_blog:
        return None

    db.delete(existing_blog)
    db.commit()
    return {"detail": f"Blog with id {id} has been deleted successfully."}