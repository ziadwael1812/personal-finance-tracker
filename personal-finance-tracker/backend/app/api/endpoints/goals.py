from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.Goal, status_code=status.HTTP_201_CREATED)
async def create_goal(
    *, 
    db: AsyncSession = Depends(deps.get_async_db),
    goal_in: schemas.GoalCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Create new goal for the current user.
    """
    goal = await crud.goal.create_with_owner(
        db=db, obj_in=goal_in, owner_id=current_user.id
    )
    return goal

@router.get("/", response_model=List[schemas.Goal])
async def read_goals(
    db: AsyncSession = Depends(deps.get_async_db),
    skip: int = 0,
    limit: int = Query(default=100, ge=1, le=200),
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Retrieve goals for the current user.
    """
    goals = await crud.goal.get_multi_by_owner(
        db, owner_id=current_user.id, skip=skip, limit=limit
    )
    return goals

@router.get("/{goal_id}", response_model=schemas.Goal)
async def read_goal(
    *, 
    db: AsyncSession = Depends(deps.get_async_db),
    goal_id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Get a specific goal by ID, owned by the current user.
    """
    goal = await crud.goal.get(db=db, id=goal_id)
    if not goal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Goal not found")
    if goal.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    return goal

@router.put("/{goal_id}", response_model=schemas.Goal)
async def update_goal(
    *, 
    db: AsyncSession = Depends(deps.get_async_db),
    goal_id: int,
    goal_in: schemas.GoalUpdate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Update a goal owned by the current user.
    """
    goal = await crud.goal.get(db=db, id=goal_id)
    if not goal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Goal not found")
    if goal.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    # Add logic here if updating goal.current_amount should be restricted or tied to transactions
    goal = await crud.goal.update(db=db, db_obj=goal, obj_in=goal_in)
    return goal

@router.delete("/{goal_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_goal(
    *, 
    db: AsyncSession = Depends(deps.get_async_db),
    goal_id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> None:
    """
    Delete a goal owned by the current user.
    """
    goal = await crud.goal.get(db=db, id=goal_id)
    if not goal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Goal not found")
    if goal.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    await crud.goal.remove(db=db, id=goal_id)
    return None 