# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class Robot(Base):
    __tablename__ = "robots"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    model_name = Column(String, index=True)

    missions = relationship("Mission", back_populates="robot")

class Mission(Base):
    __tablename__ = "missions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    robot_id = Column(Integer, ForeignKey("robots.id"))

    robot = relationship("Robot", back_populates="missions")
