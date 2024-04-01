"""
This module contains the basic models for the application
"""

from src.utils.base.libraries import BaseModel, Field, validator


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

    @validator('status_code')
    def status_code_must_be_in_range(cls, v):
        """
        Status code must be in range 100 to 599
        """
        if v < 100 or v > 599:
            raise ValueError('status code must be in range 100 to 599')
        return v

    class Config:
        """
        Configuration for the model
        """
        schema_extra = {
            "example": {
                "message": "Error message",
                "status_code": 400
            }
        }
