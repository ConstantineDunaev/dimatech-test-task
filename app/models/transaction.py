from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from app.database import Base


class Transaction(Base):
    __tablename__ = "transaction"

    transaction_id = Column(String, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    account_id = Column(Integer, ForeignKey("account.account_id"), nullable=False)
    amount = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)
