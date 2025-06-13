import pytest
from faker import Faker
from utils.logger import setup_logging
from api.client import ReqresClient


@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    setup_logging()


@pytest.fixture(scope="session")
def client():
    return ReqresClient()


@pytest.fixture(scope="session")
def faker():
    return Faker("ru_RU")


@pytest.fixture(scope="function")
def user_data(faker):
    return {"name": faker.name(), "job": faker.job()}
