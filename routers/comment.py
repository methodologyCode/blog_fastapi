from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from auth.dependencies import get_current_user
from db import db_comment
from db.database import get_db
from db.models import DbUser
from schemas.comment_schema import CommentBase

router = APIRouter(
    prefix='/comment',
    tags=['comment']
)


@router.get('/all/{post_id}')
def comments(post_id: int, db: Session = Depends(get_db)):
    return db_comment.get_all(db, post_id)


@router.post('', status_code=status.HTTP_201_CREATED)
def create(request: CommentBase, db: Session = Depends(get_db),
           current_user: DbUser = Depends(get_current_user)):
    return db_comment.create(db, request, current_user)
