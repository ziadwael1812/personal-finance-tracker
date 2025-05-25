from sqlalchemy import Column, String, Float, DateTime, ForeignKey, func, Integer, Text
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Goal(Base):
    """
    Database model for a financial Goal.
    """
    __tablename__ = "goals"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    name = Column(String, nullable=False, index=True)
    target_amount = Column(Float, nullable=False)
    current_amount = Column(Float, nullable=False, default=0.0)
    deadline = Column(DateTime, nullable=True)
    # Optional: add a description or notes for the goal
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    owner = relationship("User", back_populates="goals")

    def __repr__(self):
        return f"<Goal(id={self.id}, name='{self.name}', target_amount={self.target_amount})>" 