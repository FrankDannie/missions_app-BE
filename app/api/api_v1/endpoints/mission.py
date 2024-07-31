from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import mission as schemas
from app.crud import mission as crud
from app.db.session import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.Mission])
def read_missions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_missions(db, skip=skip, limit=limit)

@router.get("/{mission_id}", response_model=schemas.Mission)
def read_mission(mission_id: int, db: Session = Depends(get_db)):
    mission = crud.get_mission(db, mission_id=mission_id)
    if mission is None:
        raise HTTPException(status_code=404, detail="Mission not found")
    return mission

@router.post("/", response_model=schemas.Mission)
def create_mission(mission: schemas.MissionCreate, db: Session = Depends(get_db)):
    return crud.create_mission(db=db, mission=mission)

@router.put("/{mission_id}", response_model=schemas.Mission)
def update_mission(mission_id: int, mission: schemas.MissionUpdate, db: Session = Depends(get_db)):
    db_mission = crud.get_mission(db, mission_id=mission_id)
    if db_mission is None:
        raise HTTPException(status_code=404, detail="Mission not found")
    return crud.update_mission(db=db, mission=mission, mission_id=mission_id)
