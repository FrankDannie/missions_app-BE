from sqlalchemy.orm import Session
from app.models.robot import Robot as RobotModel
from app.schemas.robot import RobotCreate, RobotUpdate

def get_robots(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of robots from the database.

    Args:
        db (Session): The database session.
        skip (int): The number of records to skip (default is 0).
        limit (int): The maximum number of records to return (default is 100).

    Returns:
        List[RobotModel]: A list of robots.
    """
    return db.query(RobotModel).offset(skip).limit(limit).all()


def get_robot(db: Session, robot_id: int):
    """
    Retrieve a single robot by its ID.

    Args:
        db (Session): The database session.
        robot_id (int): The ID of the robot to retrieve.

    Returns:
        RobotModel: The robot with the specified ID, or None if not found.
    """
    return db.query(RobotModel).filter(RobotModel.id == robot_id).first()


def create_robot(db: Session, robot: RobotCreate):
    """
    Create a new robot and add it to the database.

    Args:
        db (Session): The database session.
        robot (RobotCreate): The robot data to create.

    Returns:
        RobotModel: The created robot.
    """
    db_robot = RobotModel(**robot.dict())
    db.add(db_robot)
    db.commit()
    db.refresh(db_robot)
    return db_robot


def update_robot(db: Session, robot: RobotUpdate, robot_id: int):
    """
    Update an existing robot with the provided data.

    Args:
        db (Session): The database session.
        robot (RobotUpdate): The updated robot data.
        robot_id (int): The ID of the robot to update.

    Returns:
        RobotModel: The updated robot, or None if the robot was not found.
    """
    db_robot = db.query(RobotModel).filter(RobotModel.id == robot_id).first()
    if db_robot is None:
        return None
    for key, value in robot.dict().items():
        setattr(db_robot, key, value)
    db.commit()
    db.refresh(db_robot)
    return db_robot
