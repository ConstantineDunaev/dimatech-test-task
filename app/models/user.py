from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)
    is_admin = Column(Boolean, nullable=False, default=False)
