from sqlalchemy.orm.session import Session


class CreateObject:
    model = None

    @classmethod
    def create(cls, db: Session, **param):
        new_obj = cls.model(**param)
        db.add(new_obj)
        db.commit()
        db.refresh(new_obj)
        return new_obj

    @classmethod
    def get_all(cls, db: Session, **param):
        return db.query(cls.model).filter_by(**param).all()
