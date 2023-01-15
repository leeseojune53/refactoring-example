from sqlalchemy import Column, VARCHAR, TEXT
from data.model import Base

from sqlalchemy.orm import relationship
from data.model.feed import Feed
from data.model.user import User


class Comments(Base):
    __tablename__ = 'comments'

    id = Column(VARCHAR(36), primary_key=True, nullable=True)
    content = Column(TEXT)
    feed_id = relationship(Feed, cascade="all,delete", backref="content")
    user_id = relationship(User, cascade="all,delete", backref="content")