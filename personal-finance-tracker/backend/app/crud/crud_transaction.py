from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload # For eager loading owner if needed

from app.crud.base import CRUDBase
from app.models.transaction import Transaction, TransactionType
from app.schemas.transaction import TransactionCreate, TransactionUpdate

class CRUDTransaction(CRUDBase[Transaction, TransactionCreate, TransactionUpdate]):
    async def get_multi_by_owner(
        self, db: AsyncSession, *, owner_id: int, skip: int = 0, limit: int = 100, 
        transaction_type: Optional[TransactionType] = None,
        category: Optional[str] = None
    ) -> List[Transaction]:
        query = (
            select(self.model)
            .filter(Transaction.user_id == owner_id)
            .order_by(Transaction.date.desc(), Transaction.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        if transaction_type:
            query = query.filter(Transaction.type == transaction_type)
        if category:
            query = query.filter(Transaction.category == category) # Case-sensitive, consider .ilike for case-insensitive
        
        result = await db.execute(query)
        return result.scalars().all()
    
    async def create_with_owner(
        self, db: AsyncSession, *, obj_in: TransactionCreate, owner_id: int
    ) -> Transaction:
        db_obj = self.model(**obj_in.model_dump(), user_id=owner_id)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    # get, update, remove methods are inherited from CRUDBase
    # If specific logic for update/remove is needed (e.g., ensuring user owns the transaction before update/delete),
    # those methods can be overridden here.

transaction = CRUDTransaction(Transaction) 