# models/user.py
from sqlalchemy import Column, String, Boolean
from app.database import Base
import uuid

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True)
    password_hash = Column(String)
    role = Column(String, default="viewer")
    is_active = Column(Boolean, default=True)
