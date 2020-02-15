
from sqlalchemy import Integer, String, Column, ForeignKey

from src.infrastructure.database.base import Base


class TitleModel(Base):
    """Planet model."""

    __tablename__ = 'title'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    user_id = Column('user_id', Integer, ForeignKey('user.id'))