import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from db.models import DbPost
from schemas.post_schema import PostBase, User


def create(db: Session, request: PostBase, current_user: User):
    new_post = DbPost(
        image_url=request.image_url,
        caption=request.caption,
        timestamp=datetime.datetime.now(),
        user_id=current_user.id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all(db: Session):
    return db.query(DbPost).all()


def delete(db: Session, post_id: int, user_id: int):
    post = db.query(DbPost).filter(DbPost.id == post_id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id {id} not found')

    if post.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Only post creator can delete post')

    db.delete(post)
    db.commit()
    return f'Post with ID: {post.id} deleted'
