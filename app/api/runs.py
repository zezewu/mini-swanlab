from fastapi import APIRouter, HTTPException
from datetime import datetime
from app.schemas.run import RunCreate, RunResponse

router = APIRouter(prefix="/api/runs", tags=["Runs"])

_runs = []
_id_counter = 1


@router.post("", response_model=RunResponse)
def create_run(data: RunCreate):
    global _id_counter

    run = {
        "id": _id_counter,
        "experiment_id": data.experiment_id,
        "status": "running",
        "start_time": datetime.utcnow(),
        "end_time": None
    }

    _runs.append(run)
    _id_counter += 1
    return run


@router.post("/{run_id}/finish", response_model=RunResponse)
def finish_run(run_id: int):
    for run in _runs:
        if run["id"] == run_id:
            run["status"] = "finished"
            run["end_time"] = datetime.utcnow()
            return run

    raise HTTPException(status_code=404, detail="Run not found")
