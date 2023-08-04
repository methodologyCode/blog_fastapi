from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session


class MixinObject:
    model = None

    @classmethod
    def create(cls, db: Session, **param):
        new_obj = cls.model(**param)
        db.add(new_obj)
        db.commit()
        db.refresh(new_obj)
        return new_obj

    @classmethod
    def delete(cls, db: Session, user_id: int, **param):
        obj = db.query(cls.model).filter_by(**param).first()

        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'ID - {id} not found')

        if obj.user_id != user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail='Only creator can delete')

        db.delete(obj)
        db.commit()
        return f'ID - {obj.id} deleted'

    @classmethod
    def get_all(cls, db: Session, **param):
        return db.query(cls.model).filter_by(**param).all()
