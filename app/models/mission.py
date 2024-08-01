from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Mission(Base):
    """
    SQLAlchemy model representing a mission in the database.

    Attributes:
        id (int): The unique identifier for the mission.
        name (str): The name of the mission.
        description (str): A description of the mission.
        robot_id (int): The foreign key linking to the associated robot's ID.

    Relationships:
        robot (Robot): The robot associated with this mission.
    """

    __tablename__ = "missions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    robot_id = Column(Integer, ForeignKey("robots.id"))

    robot = relationship("Robot")
