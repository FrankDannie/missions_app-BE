from sqlalchemy.orm import Session
from app.models.mission import Mission as MissionModel
from app.schemas.mission import MissionCreate, MissionUpdate

def get_missions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(MissionModel).offset(skip).all()

def get_mission(db: Session, mission_id: int):
    return db.query(MissionModel).filter(MissionModel.id == mission_id).first()

def create_mission(db: Session, mission: MissionCreate):
    db_mission = MissionModel(**mission.dict())
    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)
    return db_mission

def update_mission(db: Session, mission: MissionUpdate, mission_id: int):
    db_mission = db.query(MissionModel).filter(MissionModel.id == mission_id).first()
    if db_mission is None:
        return None
    for key, value in mission.dict().items():
        setattr(db_mission, key, value)
    db.commit()
    db.refresh(db_mission)
    return db_mission
