import re


def fetch_data(context):
    payload = context.get("payload", {})

    if not payload:
        return {
            "status": "failure",
            "message": "Missing payload"
        }

    context["fetched_data"] = payload
    return {
        "status": "success",
        "message": "Payload fetched successfully"
    }


def process_data(context):
    payload = context.get("fetched_data")

    if not payload:
        return {
            "status": "failure",
            "message": "No fetched data found"
        }

    customer_id = payload.get("customer_id")
    email = payload.get("email")

    # Validate payload
    errors = []
    email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    if not isinstance(customer_id, str) or not customer_id.strip():
        errors.append("customer_id must be a non-empty string")

    if not isinstance(email, str) or not re.match(email_pattern, email):
        errors.append("email address invalid")

    if errors:
        context["validation_errors"] = errors
        return {
            "status": "failure",
            "message": "Payload validation failed",
            "errors": errors
        }

    context["processed_data"] = {
        "customer_id": customer_id.strip(),
        "email": email.strip().lower()
    }

    return {
        "status": "success",
        "message": "Payload processed successfully"
    }

# Storing data is mocked -> context is added
def store_data(context):
    processed_data = context.get("processed_data")

    if not processed_data:
        return {
            "status": "failure",
            "message": "No processed data available to store"
        }

    context["stored"] = True
    context["store_result"] = {
        "message": "Mock save completed successfully"
    }

    return {
        "status": "success",
        "message": "Data stored successfully (mock)"
    }

# 'registry' of all tasks for the endpoint to access
TASKS = {
    "task1": fetch_data,
    "task2": process_data,
    "task3": store_data,
}