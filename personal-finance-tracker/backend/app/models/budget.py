from sqlalchemy import Column, String, Float, DateTime, ForeignKey, func, Integer
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Budget(Base):
    """
    Database model for a Budget.
    """
    __tablename__ = "budgets"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    category = Column(String, index=True, nullable=False)
    amount = Column(Float, nullable=False)
    start_date = Column(DateTime, nullable=False, default=func.now())
    end_date = Column(DateTime, nullable=False)
    name = Column(String, nullable=True) # e.g., "October 2023 Groceries"
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    owner = relationship("User", back_populates="budgets")

    def __repr__(self):
        return f"<Budget(id={self.id}, name='{self.name}', category='{self.category}', amount={self.amount})>" 