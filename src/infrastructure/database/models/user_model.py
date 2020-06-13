from sqlalchemy import Column, Integer, String, DateTime, Boolean, Date

from src.infrastructure.database.base import Base


class UserModel(Base):
    """Account model."""
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    sign_up = Column(DateTime(timezone=True), nullable=False)
    enabled = Column(Boolean, nullable=False)
    session_active = Column(DateTime(timezone=True), nullable=False)
    administrator = Column(Boolean, nullable=False)
    parental_control = Column(Boolean, nullable=False)
    birth_date = Column(Date)
