import json
from pydantic import ValidationError


def handle_error(error: Exception) -> dict:

    print(error)

    if isinstance(error, ValidationError):
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "Invalid input",
                "details": error.errors()
            })
        }
    else:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": "Internal server error"
            })
        }
