from sqlalchemy import Column, VARCHAR
from data.model import Base
import uuid


class User(Base):
    __tablename__ = 'user'

    #TODO id는 UUID로 변경
    id = Column(VARCHAR(36), primary_key=True, nullable=True)
    user_id = Column(VARCHAR(36))
    user_name = Column(VARCHAR(20))