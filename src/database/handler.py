"""
Handles all the database operations
"""

from src.utils.base.libraries import Session
from src.utils.models import NekoData


def sample_data_insertion(session: Session, data: dict) -> None:
    """
    Insert simple data in the database
    """
    session.add(NekoData(meta_data=data))
    session.commit()

    # Print the data in the console
    all_data = session.query(NekoData).all()
    for data in all_data:
        print(data.meta_data)
