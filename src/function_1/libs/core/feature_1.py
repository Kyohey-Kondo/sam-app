from pydantic import BaseModel


class AddRequestBody(BaseModel):
    operand1: int
    operand2: int


def add(body: AddRequestBody) -> int:
    return body.operand1 + body.operand2
