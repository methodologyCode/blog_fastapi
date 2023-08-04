from datetime import datetime
from typing import List

from pydantic import BaseModel

from schemas.comment_schema import Comment
from schemas.user_schema import User


class PostBase(BaseModel):
    image_url: str
    caption: str


class PostDisplay(BaseModel):
    id: int
    image_url: str
    caption: str
    timestamp: datetime
    user: User
    comments: List[Comment]

    class Config:
        orm_mode = True
