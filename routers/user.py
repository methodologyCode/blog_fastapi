from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm.session import Session

from auth.dependencies import (authenticate_user, create_access_token)
from db import db_user
from db.database import get_db
from exceptions import CannotAddDataToDatabase
from schemas.user_schema import UserBase

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post("/register", status_code=201)
def create_user(request: UserBase,
                db: Session = Depends(get_db)):
    new_user = db_user.create_user(db=db, request=request)

    if not new_user:
        raise CannotAddDataToDatabase


@router.post("/login")
def login_user(response: Response, user_data: UserBase):
    user = authenticate_user(user_data.email, user_data.password)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return {"access_token": access_token}


@router.post("/logout")
def logout_user(response: Response):
    response.delete_cookie("booking_access_token")
