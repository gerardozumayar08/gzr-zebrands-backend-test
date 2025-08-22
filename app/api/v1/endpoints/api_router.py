from fastapi import APIRouter

from app.api.v1.endpoints.auth import api_router as auth_router
from app.api.v1.endpoints.products import api_router as product_router
from app.api.v1.endpoints.users import api_router as users_router
from app.api.v1.endpoints.roles import api_router as roles_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])
api_router.include_router(product_router, prefix="/catalogs", tags=["Catalogs"])
api_router.include_router(users_router, prefix="/admin", tags=["Admin"])
api_router.include_router(roles_router, prefix="/admin", tags=["Admin"])
