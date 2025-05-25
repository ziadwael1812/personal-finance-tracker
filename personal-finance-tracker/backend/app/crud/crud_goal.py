from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.crud.base import CRUDBase
from app.models.goal import Goal
from app.schemas.goal import GoalCreate, GoalUpdate

class CRUDGoal(CRUDBase[Goal, GoalCreate, GoalUpdate]):
    async def create_with_owner(
        self, db: AsyncSession, *, obj_in: GoalCreate, owner_id: int
    ) -> Goal:
        db_obj = self.model(**obj_in.model_dump(), user_id=owner_id)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def get_multi_by_owner(
        self, db: AsyncSession, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Goal]:
        result = await db.execute(
            select(self.model)
            .filter(Goal.user_id == owner_id)
            .order_by(Goal.deadline.asc(), Goal.created_at.desc()) # Prioritize by deadline
            .offset(skip)
            .limit(limit)
        )
        return result.scalars().all()

    # get, update, remove are inherited. Override if user ownership check for update/delete is critical here.
    # Specific update logic for current_amount might be needed if it's tied to transactions.

goal = CRUDGoal(Goal) 