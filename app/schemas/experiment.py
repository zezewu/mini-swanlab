from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ExperimentCreate(BaseModel):
    name: str
    description: Optional[str] = None


class ExperimentResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    created_at: datetime
