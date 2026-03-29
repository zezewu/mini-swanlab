from fastapi import FastAPI

app = FastAPI(
    title="Mini SwanLab",
    description="A minimal experiment tracking backend inspired by SwanLab",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "Mini SwanLab backend is running"}
