from fastapi import APIRouter
from .endpoints import mission, robot

router = APIRouter()

router.include_router(mission.router, prefix="/missions", tags=["missions"])
router.include_router(robot.router, prefix="/robots", tags=["robots"])
