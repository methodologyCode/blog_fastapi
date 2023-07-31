from datetime import datetime

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from auth.dependencies import get_current_user
from db.database import get_db
from db.db_comment import Comment
from db.models import DbUser
from schemas.comment_schema import CommentBase

router = APIRouter(
    prefix='/comment',
    tags=['comment']
)


@router.get('/all/{post_id}')
def all_comments_by_post(post_id: int, db: Session = Depends(get_db)):
    return Comment.get_all(db, post_id=post_id)


@router.post('', status_code=status.HTTP_201_CREATED)
def create(request: CommentBase, db: Session = Depends(get_db),
           current_user: DbUser = Depends(get_current_user)):
    return Comment.create(db, text=request.text,
                          username=current_user.username,
                          post_id=request.post_id,
                          timestamp=datetime.now())


@router.delete('/delete/{comment_id}')
def delete(comment_id: int, db: Session = Depends(get_db),
           current_user: DbUser = Depends(get_current_user)):
    return Comment.delete(db, current_user.username, comment_id)
