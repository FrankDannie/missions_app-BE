from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import robot as schemas
from app.crud import robot as crud
from app.db.session import get_db

router = APIRouter()


@router.get("/", response_model=list[schemas.Robot])
def read_robots(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of robots with optional pagination.

    Args:
        skip (int): The number of robots to skip (default is 0).
        limit (int): The maximum number of robots to return (default is 10).
        db (Session): The database session dependency.

    Returns:
        list[schemas.Robot]: A list of robot objects.
    """
    return crud.get_robots(db, skip=skip, limit=limit)


@router.get("/{robot_id}", response_model=schemas.Robot)
def read_robot(robot_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single robot by its ID.

    Args:
        robot_id (int): The ID of the robot to retrieve.
        db (Session): The database session dependency.

    Returns:
        schemas.Robot: The robot object.

    Raises:
        HTTPException: If the robot with the given ID is not found.
    """
    robot = crud.get_robot(db, robot_id=robot_id)
    if robot is None:
        raise HTTPException(status_code=404, detail="Robot not found")
    return robot


@router.post("/", response_model=schemas.Robot)
def create_robot(robot: schemas.RobotCreate, db: Session = Depends(get_db)):
    """
    Create a new robot.

    Args:
        robot (schemas.RobotCreate): The robot data to create.
        db (Session): The database session dependency.

    Returns:
        schemas.Robot: The created robot object.
    """
    return crud.create_robot(db=db, robot=robot)


@router.put("/{robot_id}", response_model=schemas.Robot)
def update_robot(robot_id: int, robot: schemas.RobotUpdate, db: Session = Depends(get_db)):
    """
    Update an existing robot by its ID.

    Args:
        robot_id (int): The ID of the robot to update.
        robot (schemas.RobotUpdate): The updated robot data.
        db (Session): The database session dependency.

    Returns:
        schemas.Robot: The updated robot object.

    Raises:
        HTTPException: If the robot with the given ID is not found.
    """
    db_robot = crud.get_robot(db, robot_id=robot_id)
    if db_robot is None:
        raise HTTPException(status_code=404, detail="Robot not found")
    return crud.update_robot(db=db, robot=robot, robot_id=robot_id)
