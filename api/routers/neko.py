"""
Template for creating a new router
"""

from src.utils.base.libraries import (
    JSONResponse,
    APIRouter,
    Request,
    status,
    Depends,
    Session,
    BackgroundTasks
    
)
from src.database import get_db, sample_data_insertion


# Router
router = APIRouter()


# Add sample data in the database
@router.post("/sample-data", response_class=JSONResponse, tags=["Neko Nik"], summary="Add sample data in the database")
async def add_sample_data(request: Request, data: dict, background_tasks: BackgroundTasks, session: Session=Depends(get_db)) -> JSONResponse:
    """
    Add sample data in the database
    """
    background_tasks.add_task(sample_data_insertion, session, data)
    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED,
        content={"message": "Sample data added in the database"}
    )
