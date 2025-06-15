import datetime

from pydantic import BaseModel


class LoginResponse(BaseModel):
    token: str


class CreateResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: datetime.datetime


class GetResponseSupport(BaseModel):
    url: str
    text: str


class GetResponseData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class GetResponse(BaseModel):
    data: GetResponseData
    support: GetResponseSupport
