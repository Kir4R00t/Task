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
        "email": "user@example.com",
        "amount": 123,
        "currency": "eur"
    }
```

## Endpoints
```
/manager/run      - run flow (provide a json file)
/manager/tasks    - print tasks (defined in the flow manager)
/health           - health check
```

## Running the app
Run in a docker container or locally without it.

## POSTing a request
```
curl ...
```

## Example response
```
...
```