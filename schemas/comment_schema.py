from datetime import datetime

from pydantic import BaseModel


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
