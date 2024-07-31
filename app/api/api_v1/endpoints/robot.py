from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import robot as schemas
from app.crud import robot as crud
from app.db.session import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.Robot])
def read_robots(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_robots(db, skip=skip, limit=limit)

@router.get("/{robot_id}", response_model=schemas.Robot)
def read_robot(robot_id: int, db: Session = Depends(get_db)):
    robot = crud.get_robot(db, robot_id=robot_id)
    if robot is None:
        raise HTTPException(status_code=404, detail="Robot not found")
    return robot

@router.post("/", response_model=schemas.Robot)
def create_robot(robot: schemas.RobotCreate, db: Session = Depends(get_db)):
    return crud.create_robot(db=db, robot=robot)

@router.put("/{robot_id}", response_model=schemas.Robot)
def update_robot(robot_id: int, robot: schemas.RobotUpdate, db: Session = Depends(get_db)):
    db_robot = crud.get_robot(db, robot_id=robot_id)
    if db_robot is None:
        raise HTTPException(status_code=404, detail="Robot not found")
    return crud.update_robot(db=db, robot=robot, robot_id=robot_id)
