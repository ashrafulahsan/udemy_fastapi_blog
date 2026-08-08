from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Blog(BaseModel):
    title: str
    content: str
    published: Optional[bool] = True
    tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.now)

first_blog = Blog(
    title="My first blog", 
    content="This is my first blog post", 
    tags=["python", "fastapi"],
    created_at=datetime.now()
)    

print(first_blog.title)
print(first_blog.content)
print(first_blog.created_at)