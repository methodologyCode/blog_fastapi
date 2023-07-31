from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from db.models import DbComment
from db.service import CreateObject


class Comment(CreateObject):
    model = DbComment

    @classmethod
    def delete(cls, db: Session, username: str, comment_id):
        obj = db.query(cls.model).filter(cls.model.id == comment_id).first()

        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'{id} not found')

        if obj.username != username:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail='Only creator can delete')

        db.delete(obj)
        db.commit()
        return f'Comment with ID: {obj.id} deleted'
