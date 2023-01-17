from sqlalchemy import Column, VARCHAR, TEXT, TIMESTAMP, ForeignKey
from data.model import Base

from sqlalchemy.orm import relationship

from data.model.user import User


class Feed(Base):
    __tablename__ = 'feed'

    id = Column(VARCHAR(36), primary_key=True, nullable=True)
    user_id = relationship(User, cascade="all,delete", backref="feed")
    comments = Column(TEXT, ForeignKey('comments.id'))
    created_at = Column(TIMESTAMP)
