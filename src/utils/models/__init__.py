"""
All the models used in the API are defined here
"""

from .generic import All_Exceptions, Error
from .database import Base, NekoData


__version__ = "v1.0.0-phoenix-release"


__annotations__ = {
    "version": __version__,
    "All_Exceptions": "Class for handling wrong input exceptions",
    "Error": "Class for handling wrong input exceptions",
    "Base": "SQLAlchemy declarative base",
    "NekoData": "Database model for storing neko data"
}


__all__ = [
    "__version__",
    "All_Exceptions",
    "Error",
    "Base",
    "NekoData"
]
