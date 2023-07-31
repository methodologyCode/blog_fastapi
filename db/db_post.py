from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from db.models import DbPost
from db.service import CreateObject


class Post(CreateObject):
    model = DbPost

    @classmethod
    def delete(cls, db: Session, user_id: int, post_id):
        post = db.query(cls.model).filter(cls.model.id == post_id).first()

        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'Post with id {id} not found')

        if post.user_id != user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail='Only post creator can delete post')

        db.delete(post)
        db.commit()
        return f'Post with ID: {post.id} deleted'
