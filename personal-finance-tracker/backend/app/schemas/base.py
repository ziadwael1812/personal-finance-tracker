from pydantic import BaseModel
from typing import Optional, Generic, TypeVar
from datetime import datetime

class BaseSchema(BaseModel):
    class Config:
        from_attributes = True # Replaces orm_mode = True in Pydantic v2

class TimeStampedSchema(BaseSchema):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# For paginated responses
DataT = TypeVar('DataT')

class PaginatedResponse(BaseModel, Generic[DataT]):
    total: int
    page: int
    size: int
    results: list[DataT] 