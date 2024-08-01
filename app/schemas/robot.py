from pydantic import BaseModel


class RobotBase(BaseModel):
    """
    Base Pydantic model for robot data.

    Attributes:
        name (str): The name of the robot.
        model_name (str): The model name of the robot.
    """

    name: str
    model_name: str


class RobotCreate(RobotBase):
    """
    Pydantic model for creating a new robot.

    Inherits from RobotBase without any additional fields.
    """

    pass


class RobotUpdate(RobotBase):
    """
    Pydantic model for updating an existing robot.

    Inherits from RobotBase without any additional fields.
    """

    pass


class Robot(RobotBase):
    """
    Pydantic model representing a robot with its database ID.

    Attributes:
        id (int): The unique identifier of the robot.
    """

    id: int

    class Config:
        """
        Configuration for Pydantic model to support attribute-based initialization.

        This allows creating instances of Robot with attribute values directly.
        """

        from_attributes = True
