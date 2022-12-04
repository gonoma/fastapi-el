# coding: utf-8
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship  # For later use

from src.database.base import BaseModel


class User(BaseModel):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'users'}

    email = Column(String(255), primary_key=True)
    username = Column(String(36), unique=True, nullable=False)
    full_name = Column(String(255), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    disabled = Column(Boolean, default=True, nullable=False)
