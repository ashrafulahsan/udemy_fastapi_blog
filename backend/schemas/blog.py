from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field, model_validator
from datetime import datetime

class CreateBlog(BaseModel):
    title: str
    slug: Optional[str] = None
    content: str
    published: Optional[bool] = True
    created_at: Optional[datetime] = Field(default_factory=datetime.now)

    @model_validator(mode="before")
    @classmethod
    def generate_slug(cls, values: Any) -> Any:
        if not isinstance(values, dict):
            return values
        title = values.get('title')
        if title and not values.get('slug'):
            values['slug'] = title.lower().replace(' ', '-')
        return values

class UpdateBlog(CreateBlog):
    pass


class ShowBlog(BaseModel):
    id: int
    title: str
    slug: str
    content: str
    published: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)