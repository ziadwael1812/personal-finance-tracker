from fastapi import APIRouter

from app.api.endpoints import auth, users #, other_endpoints

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
# Add other routers here
# api_router.include_router(other_endpoints.router, prefix="/items", tags=["Items"]) 