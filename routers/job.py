import uuid
from typing import Optional
from fastapi import APIRouter,Depends,HTTPException,Cookie
from sqlalchemy .orm import Session

from models.job import StroyJob
from schemas.job import StoryJobResponse
from db.database import get_db

router=APIRouter(
    prefix="/jobs",
    tags=["jobs"]
)

@router.get("/{job_id}",response_model=StoryJobResponse)
def get_job_status(job_id:str,db:Session=Depends(get_db)):
    job=db.query(StroyJob).filter(StroyJob.job_id==job_id).first()

    if not job:
        raise HTTPException(status_cde=404,detail="Job not found")
    return job