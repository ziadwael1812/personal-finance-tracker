from typing import Any, List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud, models, schemas
from app.api import deps
from app.models.transaction import TransactionType # For query param validation

router = APIRouter()

@router.post("/", response_model=schemas.Transaction, status_code=status.HTTP_201_CREATED)
async def create_transaction(
    *, 
    db: AsyncSession = Depends(deps.get_async_db),
    transaction_in: schemas.TransactionCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Create new transaction for the current user.
    """
    transaction = await crud.transaction.create_with_owner(
        db=db, obj_in=transaction_in, owner_id=current_user.id
    )
    # Optional: Update goal current_amount if transaction is related to a goal
    return transaction

@router.get("/", response_model=List[schemas.Transaction])
async def read_transactions(
    db: AsyncSession = Depends(deps.get_async_db),
    skip: int = 0,
    limit: int = Query(default=100, ge=1, le=200),
    transaction_type: Optional[TransactionType] = Query(default=None, description="Filter by transaction type (income or expense)"),
    category: Optional[str] = Query(default=None, min_length=1, max_length=100, description="Filter by category (case-sensitive)"),
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Retrieve transactions for the current user, with optional filters.
    """
    transactions = await crud.transaction.get_multi_by_owner(
        db, owner_id=current_user.id, skip=skip, limit=limit, transaction_type=transaction_type, category=category
    )
    return transactions

@router.get("/{transaction_id}", response_model=schemas.Transaction)
async def read_transaction(
    *, 
    db: AsyncSession = Depends(deps.get_async_db),
    transaction_id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Get a specific transaction by ID, owned by the current user.
    """
    transaction = await crud.transaction.get(db=db, id=transaction_id)
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found")
    if transaction.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    return transaction

@router.put("/{transaction_id}", response_model=schemas.Transaction)
async def update_transaction(
    *, 
    db: AsyncSession = Depends(deps.get_async_db),
    transaction_id: int,
    transaction_in: schemas.TransactionUpdate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Update a transaction owned by the current user.
    """
    transaction = await crud.transaction.get(db=db, id=transaction_id)
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found")
    if transaction.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    transaction = await crud.transaction.update(db=db, db_obj=transaction, obj_in=transaction_in)
    return transaction

@router.delete("/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_transaction(
    *, 
    db: AsyncSession = Depends(deps.get_async_db),
    transaction_id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> None:
    """
    Delete a transaction owned by the current user.
    """
    transaction = await crud.transaction.get(db=db, id=transaction_id)
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found")
    if transaction.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    await crud.transaction.remove(db=db, id=transaction_id)
    return None # FastAPI will return 204 No Content 