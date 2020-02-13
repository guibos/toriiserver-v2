from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.database.base import Base
from src.database.models.title_model import TitleModel


class UserModel(Base):
    """Account model."""
    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True)
    username = Column('name', String)

    titles = relationship(TitleModel, backref='user')
