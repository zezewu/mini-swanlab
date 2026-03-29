from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class RunCreate(BaseModel):
    experiment_id: int


class RunResponse(BaseModel):
    id: int
    experiment_id: int
    status: str
    start_time: datetime
    end_time: Optional[datetime]
