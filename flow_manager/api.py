from typing import Dict
from fastapi import FastAPI

app = FastAPI

'''
/manager/run      - run flow (provide a json file)
/manager/tasks    - print tasks (defined in the flow manager)
'''

@app.get("/health")
def healthcheck() -> Dict:
    return {"status": "ok"}
