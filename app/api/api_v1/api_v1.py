from fastapi import APIRouter
from .endpoints import mission

router = APIRouter()

router.include_router(mission.router, prefix="/missions", tags=["missions"])
