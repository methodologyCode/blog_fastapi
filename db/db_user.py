from sqlalchemy import select
from sqlalchemy.orm.session import Session

from auth import dependencies
from db.database import SessionLocal
from db.models import DbUser
from schemas.user_schema import UserBase


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=dependencies.get_password_hash(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def find_one_or_none(**filter_by):
    with SessionLocal() as session:
        query = select(DbUser.__table__.columns).filter_by(**filter_by)
        result = session.execute(query)
        return result.first()
