from sqlalchemy.orm import Session
from app.models.robot import Robot as RobotModel
from app.schemas.robot import RobotCreate, RobotUpdate

def get_robots(db: Session, skip: int = 0, limit: int = 100):
    return db.query(RobotModel).offset(skip).all()

def get_robot(db: Session, robot_id: int):
    return db.query(RobotModel).filter(RobotModel.id == robot_id).first()

def create_robot(db: Session, robot: RobotCreate):
    db_robot = RobotModel(**robot.dict())
    db.add(db_robot)
    db.commit()
    db.refresh(db_robot)
    return db_robot

def update_robot(db: Session, robot: RobotUpdate, robot_id: int):
    db_robot = db.query(RobotModel).filter(RobotModel.id == robot_id).first()
    if db_robot is None:
        return None
    for key, value in robot.dict().items():
        setattr(db_robot, key, value)
    db.commit()
    db.refresh(db_robot)
    return db_robot
