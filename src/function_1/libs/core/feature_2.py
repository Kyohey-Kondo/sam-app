from pydantic import BaseModel


class MultipleRequestBody(BaseModel):
    operand1: int
    operand2: int


def multiple(body: MultipleRequestBody) -> int:
    return body.operand1 * body.operand2
