from sqlalchemy import Column, Integer, ForeignKey, String
from app.database import Base


class Account(Base):
    __tablename__ = "account"

    account_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    name = Column(String, nullable=False)
