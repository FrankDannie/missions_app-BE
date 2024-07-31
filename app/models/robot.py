from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Robot(Base):
    __tablename__ = 'robots'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    model_name = Column(String)
