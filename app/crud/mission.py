from sqlalchemy.orm import Session
from app.models.mission import Mission as MissionModel
from app.schemas.mission import MissionCreate, MissionUpdate

def get_missions(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of missions from the database.

    Args:
        db (Session): The database session.
        skip (int): The number of records to skip (default is 0).
        limit (int): The maximum number of records to return (default is 10).

    Returns:
        List[MissionModel]: A list of missions.
    """
    return db.query(MissionModel).offset(skip).limit(limit).all()


def get_mission(db: Session, mission_id: int):
    """
    Retrieve a single mission by its ID.

    Args:
        db (Session): The database session.
        mission_id (int): The ID of the mission to retrieve.

    Returns:
        MissionModel: The mission with the specified ID, or None if not found.
    """
    return db.query(MissionModel).filter(MissionModel.id == mission_id).first()


def create_mission(db: Session, mission: MissionCreate):
    """
    Create a new mission and add it to the database.

    Args:
        db (Session): The database session.
        mission (MissionCreate): The mission data to create.

    Returns:
        MissionModel: The created mission.
    """
    db_mission = MissionModel(**mission.dict())
    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)
    return db_mission


def update_mission(db: Session, mission: MissionUpdate, mission_id: int):
    """
    Update an existing mission with the provided data.

    Args:
        db (Session): The database session.
        mission (MissionUpdate): The updated mission data.
        mission_id (int): The ID of the mission to update.

    Returns:
        MissionModel: The updated mission, or None if the mission was not found.
    """
    db_mission = db.query(MissionModel).filter(MissionModel.id == mission_id).first()
    if db_mission is None:
        return None
    for key, value in mission.dict().items():
        setattr(db_mission, key, value)
    db.commit()
    db.refresh(db_mission)
    return db_mission
