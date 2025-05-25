from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.crud.base import CRUDBase
from app.models.budget import Budget
from app.schemas.budget import BudgetCreate, BudgetUpdate

class CRUDBudget(CRUDBase[Budget, BudgetCreate, BudgetUpdate]):
    async def create_with_owner(
        self, db: AsyncSession, *, obj_in: BudgetCreate, owner_id: int
    ) -> Budget:
        db_obj = self.model(**obj_in.model_dump(), user_id=owner_id)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def get_multi_by_owner(
        self, db: AsyncSession, *, owner_id: int, skip: int = 0, limit: int = 100,
        # Add any specific filters for budgets if needed, e.g., by category or date range
        category: Optional[str] = None 
    ) -> List[Budget]:
        query = (
            select(self.model)
            .filter(Budget.user_id == owner_id)
            .order_by(Budget.start_date.desc()) # Or by name, etc.
            .offset(skip)
            .limit(limit)
        )
        if category:
            query = query.filter(Budget.category == category)
        result = await db.execute(query)
        return result.scalars().all()

    # get, update, remove are inherited. Override if user ownership check for update/delete is critical here.


budget = CRUDBudget(Budget) 