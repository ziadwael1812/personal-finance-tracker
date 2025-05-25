from pydantic import Field
from typing import Optional
from datetime import datetime
from .base import BaseSchema, TimeStampedSchema

# Shared properties
class BudgetBase(BaseSchema):
    category: Optional[str] = None
    amount: Optional[float] = Field(default=None, gt=0)
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    name: Optional[str] = None

# Properties to receive on creation
class BudgetCreate(BudgetBase):
    category: str
    amount: float = Field(gt=0)
    start_date: datetime = Field(default_factory=datetime.utcnow)
    end_date: datetime
    name: Optional[str] = None

# Properties to receive on update
class BudgetUpdate(BudgetBase):
    pass # All fields are optional

# Properties stored in DB
class BudgetInDBBase(TimeStampedSchema, BudgetBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True

# Additional properties to return via API
class Budget(BudgetInDBBase):
    pass 