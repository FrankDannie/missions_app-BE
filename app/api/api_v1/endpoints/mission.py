from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import mission as schemas
from app.crud import mission as crud
from app.db.session import get_db

router = APIRouter()


@router.get("/", response_model=list[schemas.Mission])
def read_missions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of missions with optional pagination.

    Args:
        skip (int): The number of missions to skip (default is 0).
        limit (int): The maximum number of missions to return (default is 10).
        db (Session): The database session dependency.

    Returns:
        list[schemas.Mission]: A list of mission objects.
    """
    return crud.get_missions(db, skip=skip, limit=limit)


@router.get("/{mission_id}", response_model=schemas.Mission)
def read_mission(mission_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single mission by its ID.

    Args:
        mission_id (int): The ID of the mission to retrieve.
        db (Session): The database session dependency.

    Returns:
        schemas.Mission: The mission object.

    Raises:
        HTTPException: If the mission with the given ID is not found.
    """
    mission = crud.get_mission(db, mission_id=mission_id)
    if mission is None:
        raise HTTPException(status_code=404, detail="Mission not found")
    return mission


@router.post("/", response_model=schemas.Mission)
def create_mission(mission: schemas.MissionCreate, db: Session = Depends(get_db)):
    """
    Create a new mission.

    Args:
        mission (schemas.MissionCreate): The mission data to create.
        db (Session): The database session dependency.

    Returns:
        schemas.Mission: The created mission object.
    """
    return crud.create_mission(db=db, mission=mission)


@router.put("/{mission_id}", response_model=schemas.Mission)
def update_mission(mission_id: int, mission: schemas.MissionUpdate, db: Session = Depends(get_db)):
    """
    Update an existing mission by its ID.

    Args:
        mission_id (int): The ID of the mission to update.
        mission (schemas.MissionUpdate): The updated mission data.
        db (Session): The database session dependency.

    Returns:
        schemas.Mission: The updated mission object.

    Raises:
        HTTPException: If the mission with the given ID is not found.
    """
    db_mission = crud.get_mission(db, mission_id=mission_id)
    if db_mission is None:
        raise HTTPException(status_code=404, detail="Mission not found")
    return crud.update_mission(db=db, mission=mission, mission_id=mission_id)
