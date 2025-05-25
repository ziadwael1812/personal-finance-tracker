from pydantic import Field
from typing import Optional
from datetime import datetime
from .base import BaseSchema, TimeStampedSchema

# Shared properties
class GoalBase(BaseSchema):
    name: Optional[str] = None
    target_amount: Optional[float] = Field(default=None, gt=0)
    current_amount: Optional[float] = Field(default=0.0, ge=0)
    deadline: Optional[datetime] = None
    description: Optional[str] = None

# Properties to receive on creation
class GoalCreate(GoalBase):
    name: str
    target_amount: float = Field(gt=0)
    current_amount: float = Field(default=0.0, ge=0)
    deadline: Optional[datetime] = None
    description: Optional[str] = None

# Properties to receive on update
class GoalUpdate(GoalBase):
    # current_amount can be updated directly or via transactions later
    current_amount: Optional[float] = Field(default=None, ge=0)

# Properties stored in DB
class GoalInDBBase(TimeStampedSchema, GoalBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True

# Additional properties to return via API
class Goal(GoalInDBBase):
    pass 