"""
All the Database related functions are defined here
"""

from .connections import init_db, get_db
from .handler import sample_data_insertion


__version__ = "v1.0.0-phoenix-release"


__annotations__ = {
    "version": __version__,
    "init_db": "Function to initialize the database",
    "get_db": "Function to get the database session",
    "sample_data_insertion": "Function to insert sample data in the database"
}


__all__ = [
    "__version__",
    "init_db",
    "get_db",
    "sample_data_insertion"
]
