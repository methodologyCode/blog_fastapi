from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDisplay(BaseModel):
    id: int
    username: str
    email: EmailStr


# For PostDisplay/CommentDisplay
class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
