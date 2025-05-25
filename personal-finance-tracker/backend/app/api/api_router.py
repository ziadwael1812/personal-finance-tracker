from fastapi import APIRouter

from app.api.endpoints import auth, users, transactions, budgets, goals

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])
api_router.include_router(budgets.router, prefix="/budgets", tags=["Budgets"])
api_router.include_router(goals.router, prefix="/goals", tags=["Goals"])
# Add other routers here
# api_router.include_router(other_endpoints.router, prefix="/items", tags=["Items"]) 