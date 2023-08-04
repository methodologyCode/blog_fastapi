from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from auth.dependencies import get_current_user
from db.database import get_db
from db.db_post import Post
from db.models import DbUser
from schemas.post_schema import PostBase, PostDisplay

router = APIRouter(
    prefix='/post',
    tags=['post']
)


@router.post('', status_code=status.HTTP_201_CREATED)
def create(request: PostBase, db: Session = Depends(get_db),
           current_user: DbUser = Depends(get_current_user)) -> PostDisplay:
    return Post.create(db, image_url=request.image_url,
                       caption=request.caption,
                       timestamp=datetime.now(),
                       user_id=current_user.id)


@router.get('/all')
def get_all_posts(db: Session = Depends(get_db)) -> List[PostDisplay]:
    return Post.get_all(db)


@router.delete('/delete/{post_id}')
def delete(post_id: int, db: Session = Depends(get_db),
           current_user: DbUser = Depends(get_current_user)):
    return Post.delete(db, current_user.id, id=post_id)
