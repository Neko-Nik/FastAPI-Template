"""
This module contains the basic models for the application
"""

from src.utils.base.libraries import BaseModel, Field


class All_Exceptions(Exception):
    """Class for handling wrong input exceptions"""
    def __init__(self , message: str , status_code: int):
        self.message = message
        self.status_code = status_code


class Error(BaseModel):
    """
    Error model for API, if any error occurs, this model is returned
    Error message and status code is returned
    message: Error message
    status_code: Error status code
    """
    message: str = Field(..., title="Message", description="Error message")
    status_code: int = Field(..., title="Status Code", description="Error status code")

    class Config:
        """
        Configuration for the model
        """
        json_schema_extra = {
            "example": {
                "message": "Error message",
                "status_code": 400
            }
        }
