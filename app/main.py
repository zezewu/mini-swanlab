from fastapi import FastAPI
from app.api.experiments import router as experiment_router
from app.api.runs import router as run_router

# ✅ 先创建 FastAPI 实例
app = FastAPI(
    title="Mini SwanLab",
    description="A minimal experiment tracking backend inspired by SwanLab",
    version="0.1.0"
)

# ✅ 再注册 router
app.include_router(experiment_router)
app.include_router(run_router)


@app.get("/")
def root():
    return {"message": "Mini SwanLab backend is running"}
