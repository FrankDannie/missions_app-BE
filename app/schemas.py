# app/schemas.py

from pydantic import BaseModel
from typing import List, Optional

class RobotBase(BaseModel):
    name: str
    model_name: str

class RobotCreate(RobotBase):
    pass

class Robot(RobotBase):
    id: int

    class Config:
        orm_mode = True

class MissionBase(BaseModel):
    name: str
    description: str

class MissionCreate(MissionBase):
    robot_id: int  # Use robot_id to avoid cyclic references

class Mission(MissionBase):
    id: int
    robot: Robot  

    class Config:
        orm_mode = True
