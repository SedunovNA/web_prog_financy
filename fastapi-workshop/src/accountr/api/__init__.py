# api/__init__.py
from fastapi import APIRouter
from .auth import router as auth_router
from .operations import router as operations_router
from .reports import router as reports_router
from .wallet import router as wallet_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(operations_router)
router.include_router(reports_router)
router.include_router(wallet_router)
