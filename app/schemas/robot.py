from pydantic import BaseModel

class RobotBase(BaseModel):
    name: str
    model_name: str

class RobotCreate(RobotBase):
    pass

class RobotUpdate(RobotBase):
    pass

class Robot(RobotBase):
    id: int

    class Config:
        from_attributes = True
