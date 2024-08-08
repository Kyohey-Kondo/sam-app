import json

from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyEvent
from aws_lambda_powertools.utilities.typing import LambdaContext

from src.function_1.libs.core import feature_1, feature_2, AddRequestBody, MultipleRequestBody
from src.function_1.libs.utils import handle_error, response


def lambda_handler(event: APIGatewayProxyEvent, context: LambdaContext):

    event = APIGatewayProxyEvent(event)

    path = event.path
    body = json.loads(event.body)

    try:
        match path:
            case "/feature_1":
                body = AddRequestBody(**body)
                result = feature_1.add(body)
                return response(200, result)
            case "/feature_2":
                body = MultipleRequestBody(**body)
                result = feature_2.multiple(body)
                return response(200, result)

        return response(200, "hello world")

    except Exception as e:
        return handle_error(e)
