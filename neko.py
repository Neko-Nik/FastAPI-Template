"""
Sample read file from the Local DB
"""

from src.utils.base.libraries import create_engine, sessionmaker
from src.utils.models import NekoData

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(url=SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fetch all the data from the database
all_data = SessionLocal().query(NekoData).all()

for data in all_data:
    print(data.meta_data)
