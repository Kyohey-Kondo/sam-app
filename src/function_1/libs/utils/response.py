import json


def response(status_code: int, result: dict) -> dict:

    return {
        "statusCode": status_code,
        "body": json.dumps({
            "result": result,
        }),
    }
