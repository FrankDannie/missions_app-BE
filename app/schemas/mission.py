from pydantic import BaseModel

class MissionBase(BaseModel):
    name: str
    description: str
    robot_id: int

class MissionCreate(MissionBase):
    pass

class MissionUpdate(MissionBase):
    pass

class Mission(MissionBase):
    id: int

    class Config:
        from_attributes = True
