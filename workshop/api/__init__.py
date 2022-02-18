from fastapi import APIRouter

from .auth import router as auth_router
from .operations import router as operations_router
from .reports import router as reports_router

router = APIRouter(prefix='/api')
router.include_router(operations_router)
router.include_router(auth_router)
router.include_router(reports_router)
