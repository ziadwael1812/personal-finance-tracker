from typing import Any, List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.Budget, status_code=status.HTTP_201_CREATED)
async def create_budget(
    *, 
    db: AsyncSession = Depends(deps.get_async_db),
    budget_in: schemas.BudgetCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Create new budget for the current user.
    """
    budget = await crud.budget.create_with_owner(
        db=db, obj_in=budget_in, owner_id=current_user.id
    )
    return budget

@router.get("/", response_model=List[schemas.Budget])
async def read_budgets(
    db: AsyncSession = Depends(deps.get_async_db),
    skip: int = 0,
    limit: int = Query(default=100, ge=1, le=200),
    category: Optional[str] = Query(default=None, min_length=1, max_length=100, description="Filter by category (case-sensitive)"),
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Retrieve budgets for the current user.
    """
    budgets = await crud.budget.get_multi_by_owner(
        db, owner_id=current_user.id, skip=skip, limit=limit, category=category
    )
    return budgets

@router.get("/{budget_id}", response_model=schemas.Budget)
async def read_budget(
    *, 
    db: AsyncSession = Depends(deps.get_async_db),
    budget_id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Get a specific budget by ID, owned by the current user.
    """
    budget = await crud.budget.get(db=db, id=budget_id)
    if not budget:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Budget not found")
    if budget.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    return budget

@router.put("/{budget_id}", response_model=schemas.Budget)
async def update_budget(
    *, 
    db: AsyncSession = Depends(deps.get_async_db),
    budget_id: int,
    budget_in: schemas.BudgetUpdate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Update a budget owned by the current user.
    """
    budget = await crud.budget.get(db=db, id=budget_id)
    if not budget:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Budget not found")
    if budget.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    budget = await crud.budget.update(db=db, db_obj=budget, obj_in=budget_in)
    return budget

@router.delete("/{budget_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_budget(
    *, 
    db: AsyncSession = Depends(deps.get_async_db),
    budget_id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> None:
    """
    Delete a budget owned by the current user.
    """
    budget = await crud.budget.get(db=db, id=budget_id)
    if not budget:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Budget not found")
    if budget.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    await crud.budget.remove(db=db, id=budget_id)
    return None 