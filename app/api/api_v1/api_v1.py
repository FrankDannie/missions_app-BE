from fastapi import APIRouter
from .endpoints import mission, robot

router = APIRouter()

"""
    Route for listing all mission-related endpoints.

    Includes routes for:
    - Retrieving a list of missions
    - Retrieving a single mission by ID
    - Creating a new mission
    - Updating an existing mission
    """
router.include_router(mission.router, prefix="/missions", tags=["missions"])

"""
    Route for listing all robot-related endpoints.

    Includes routes for:
    - Retrieving a list of robots
    - Retrieving a single robot by ID
    - Creating a new robot
    - Updating an existing robot
    """
router.include_router(robot.router, prefix="/robots", tags=["robots"])
