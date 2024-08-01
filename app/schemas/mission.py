from pydantic import BaseModel


class MissionBase(BaseModel):
    """
    Base Pydantic model for mission data.

    Attributes:
        name (str): The name of the mission.
        description (str): The description of the mission.
        robot_id (int): The ID of the robot associated with the mission.
    """

    name: str
    description: str
    robot_id: int


class MissionCreate(MissionBase):
    """
    Pydantic model for creating a new mission.

    Inherits from MissionBase without any additional fields.
    """

    pass


class MissionUpdate(MissionBase):
    """
    Pydantic model for updating an existing mission.

    Inherits from MissionBase without any additional fields.
    """

    pass


class Mission(MissionBase):
    """
    Pydantic model representing a mission with its database ID.

    Attributes:
        id (int): The unique identifier of the mission.
    """

    id: int

    class Config:
        """
        Configuration for Pydantic model to support attribute-based initialization.

        This allows creating instances of Mission with attribute values directly.
        """

        from_attributes = True
