from pydantic import BaseModel


class HTTPResponse(BaseModel):
    code: int
    detail: str
