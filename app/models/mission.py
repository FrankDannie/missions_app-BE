from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Mission(Base):
    __tablename__ = 'missions'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    robot_id = Column(Integer, ForeignKey('robots.id'))
    
    robot = relationship("Robot")
