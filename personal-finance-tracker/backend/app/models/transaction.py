from sqlalchemy import Column, String, Float, DateTime, ForeignKey, Enum as SAEnum, Text, func
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum

class TransactionType(str, enum.Enum):
    INCOME = "income"
    EXPENSE = "expense"

class Transaction(Base):
    """
    Database model for a Transaction.
    """
    __tablename__ = "transactions"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    amount = Column(Float, nullable=False)
    category = Column(String, index=True, nullable=False)
    type = Column(SAEnum(TransactionType), nullable=False, index=True)
    date = Column(DateTime, nullable=False, index=True, default=func.now())
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    owner = relationship("User", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction(id={self.id}, type='{self.type}', amount={self.amount}, category='{self.category}')>" 