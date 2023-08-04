from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from .database import Base


class DbUser(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    items = relationship('DbPost', back_populates='user')
    comment = relationship('DbComment', back_populates='user')


class DbPost(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('DbUser', back_populates='items')
    comments = relationship('DbComment', back_populates='post')


class DbComment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    username = Column(String)
    timestamp = Column(DateTime)
    post_id = Column(Integer, ForeignKey('posts.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    post = relationship("DbPost", back_populates="comments")
    user = relationship('DbUser', back_populates='comment')
