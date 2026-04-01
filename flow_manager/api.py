from typing import Dict
from fastapi import FastAPI, HTTPException

from flow_manager.flow_manager import FlowManager
from flow_manager.tasks import TASKS

app = FastAPI()

@app.get("/health")
def healthcheck() -> Dict:
    return {"status": "ok"}

@app.get("/manager/tasks")
def get_tasks() -> Dict:
    return {"available_tasks": list(TASKS.keys())} # TODO: should return values (func names)

@app.post("/manager/run")
def run_flow(flow_data: Dict):
    try:
        manager = FlowManager(flow_data)
        return manager.execute_flow()
    
    except KeyError as exc:
        raise HTTPException(status_code=400, detail=f"Missing required field: {str(exc)}")
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))