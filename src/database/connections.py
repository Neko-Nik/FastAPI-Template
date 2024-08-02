"""
This file contains the database connection and session creation functions
"""

from src.utils.base.libraries import create_engine, sessionmaker, Depends, status, APIKeyHeader
from src.utils.base.constants import POSTGRES_DB_DATABASE, POSTGRES_DB_HOST, POSTGRES_DB_PASSWORD, POSTGRES_DB_PORT, POSTGRES_DB_USERNAME, INTERNAL_API_KEY
from src.utils.models import Base, All_Exceptions


# For SQLite local database
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(url=SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# For Postgres database (production)
# engine = create_engine(url=f"postgresql://{POSTGRES_DB_USERNAME}:{POSTGRES_DB_PASSWORD}@{POSTGRES_DB_HOST}:{POSTGRES_DB_PORT}/{POSTGRES_DB_DATABASE}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def _validate_key(api_key: str) -> None:
    if api_key != INTERNAL_API_KEY:
        raise All_Exceptions(
            message="Invalid API Key!",
            status_code=status.HTTP_401_UNAUTHORIZED
        )


def init_db():
    """
    Function to initialize the database
    """
    Base.metadata.create_all(bind=engine, checkfirst=True)
    # Registering event listeners on specific models to handle database events like insert, update, delete here


def get_db(api_key: str = Depends(APIKeyHeader(name="N-Api-Key"))):
    """
    Function to get the database session
    Used in the FastAPI dependency injection system
    """
    # Validating the API key (Integrating API key validation)
    _validate_key(api_key=api_key)
    # Creating a new session for each request
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
