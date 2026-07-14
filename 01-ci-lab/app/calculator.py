import json


def add(a, b):
    return a + b


def divide(a, b):
    return a / b


def multiply(a, b):
    return a * b


def subtract(a, b):
    return a - b


def power(a, b):
    return a ** b


def lambda_handler(event, context):
    # function URL / API Gateway
    if "body" in event:
        if isinstance(event["body"], str):
            body = json.loads(event["body"])
        else:
            body = event["body"]
    # test from AWS console
    else:
        body = event

    a = float(body["a"])
    b = float(body["b"])
    operation = body["operation"]

    if operation == 'add':
        result = add(a, b)
    elif operation == 'divide':
        result = divide(a, b)
    elif operation == 'multiply':
        result = multiply(a, b)
    elif operation == "substract":
        result = subtract(a, b)
    elif operation == "power":
        result = power(a, b)
    else:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Unsupported operation"})
        }

    return {
        "statusCode": 200,
        "body": json.dumps({"result": result})
    }
