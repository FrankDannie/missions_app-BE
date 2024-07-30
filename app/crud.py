# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def get_mission(db: Session, mission_id: int):
    return db.query(models.Mission).filter(models.Mission.id == mission_id).first()

def get_missions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Mission).offset(skip).limit(limit).all()

def create_mission(db: Session, mission: schemas.MissionCreate):
    db_mission = models.Mission(**mission.dict())
    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)
    return db_mission

def get_robot(db: Session, robot_id: int):
    return db.query(models.Robot).filter(models.Robot.id == robot_id).first()

def get_robots(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Robot).offset(skip).limit(limit).all()

def create_robot(db: Session, robot: schemas.RobotCreate):
    db_robot = models.Robot(**robot.dict())
    db.add(db_robot)
    db.commit()
    db.refresh(db_robot)
    return db_robot
