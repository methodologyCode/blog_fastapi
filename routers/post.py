from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from auth.dependencies import get_current_user
from db import db_post
from db.database import get_db
from db.models import DbUser
from schemas.post_schema import PostBase, PostDisplay

router = APIRouter(
    prefix='/post',
    tags=['post']
)


@router.post('', status_code=status.HTTP_201_CREATED)
def create(request: PostBase, db: Session = Depends(get_db),
           current_user: DbUser = Depends(get_current_user)) -> PostDisplay:
    return db_post.create(db, request, current_user)


@router.get('/all')
def posts(db: Session = Depends(get_db)) -> List[PostDisplay]:
    return db_post.get_all(db)


@router.delete('/delete/{post_id}')
def delete(post_id: int, db: Session = Depends(get_db),
           current_user: DbUser = Depends(get_current_user)):
    return db_post.delete(db, post_id, current_user.id)
