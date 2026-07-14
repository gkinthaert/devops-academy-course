def add(a, b):
    return a + b


def divide(a, b):
    return a / b


def multiply(a, b):
    return a * b


def lambda_handler(event, context):
    operation = event.get('operation')
    a = event.get('a')
    b = event.get('b')

    if operation == 'add':
        result = add(a, b)
    elif operation == 'divide':
        result = divide(a, b)
    elif operation == 'multiply':
        result = multiply(a, b)
    else:
        return {
            'statusCode': 400,
            'body': 'Invalid operation'
        }

    return {
        'statusCode': 200,
        'body': result
    }
