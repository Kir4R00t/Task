def fetch_data():
    pass

def process_data():
    pass

def store_data():
    pass

# 'registry' of all tasks for the endpoint to access
TASKS = {
    "fetch_data": fetch_data,
    "process_data": process_data,
    "store_data": store_data,
}