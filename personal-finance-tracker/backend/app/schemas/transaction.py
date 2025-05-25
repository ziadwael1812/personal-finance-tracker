from pydantic import Field
from typing import Optional
from datetime import datetime
from app.models.transaction import TransactionType # Import the enum from models
from .base import BaseSchema, TimeStampedSchema

# Shared properties
class TransactionBase(BaseSchema):
    amount: Optional[float] = Field(default=None, gt=0)
    category: Optional[str] = None
    type: Optional[TransactionType] = None
    date: Optional[datetime] = None
    description: Optional[str] = None

# Properties to receive on creation
class TransactionCreate(TransactionBase):
    amount: float = Field(gt=0)
    category: str
    type: TransactionType
    date: datetime = Field(default_factory=datetime.utcnow)

# Properties to receive on update
class TransactionUpdate(TransactionBase):
    pass # All fields are optional as defined in TransactionBase

# Properties stored in DB
class TransactionInDBBase(TimeStampedSchema, TransactionBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True

# Additional properties to return via API
class Transaction(TransactionInDBBase):
    pass 