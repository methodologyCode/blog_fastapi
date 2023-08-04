from datetime import datetime

from pydantic import BaseModel

from schemas.user_schema import User


class CommentBase(BaseModel):
    text: str
    post_id: int


# For PostDisplay
class Comment(BaseModel):
    text: str
    username: str
    timestamp: datetime

    class Config:
        orm_mode = True


class CommentDisplay(BaseModel):
    text: str
    timestamp: datetime
    user: User

    class Config:
        orm_mode = True
