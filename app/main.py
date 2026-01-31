from fastapi import FastAPI
from app.agent import solve_task

app = FastAPI(title="Purple Agent Baseline")

@app.post("/a2a/solve")
def solve(task: dict):
    result = solve_task(task)
    return {
        "status": "success",
        "result": result
    }

@app.get("/health")
def health():
    return {"status": "ok"}
