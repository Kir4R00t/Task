# Task
Flow manager app.

## App structure
```
flow_manager/
|── flow_manager.py     # Core
|── tasks.py            # Task implementation
|── api.py              # FastAPI endpoints
```

## example.json
This file contains the flow. 
I added 'payload' object just to have 'actual' data to parse.
```
"payload": {
    "customer_id": "123",
    "email": "user@example.com"
}
```

## Endpoints
```
/manager/run      - run flow (provide a json file)
/manager/tasks    - print tasks (defined in the flow manager)
/health           - health check
```

## Running the app
Docker container - completely optional, however fitting for this kind of project :)
```
cd flow_manager/
docker compose up --build
```

Locally (uvicorn)
```
cd flow_manager/
uvicorn flow_manager.api:app --reload
```

## POSTing a request
You can POST the flow either using `curl` or via the swagger at `http://127.0.0.1:8000/docs`.
```
curl -X POST "http://127.0.0.1:8000/manager/run" `
     -H "Content-Type: application/json" `
     -d "@example.json"
```