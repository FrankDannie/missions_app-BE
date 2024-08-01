from sqlalchemy import Column, Integer, String
from app.db.base import Base


class Robot(Base):
    """
    SQLAlchemy model representing a robot in the database.

    Attributes:
        id (int): The unique identifier for the robot.
        name (str): The name of the robot.
        model_name (str): The model name of the robot.
    """

    __tablename__ = "robots"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    model_name = Column(String)
