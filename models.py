import datetime

from pydantic import BaseModel


class LoginResponse(BaseModel):
    token: str


class CreateResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: datetime.datetime
