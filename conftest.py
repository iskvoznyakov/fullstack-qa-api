import pytest
from utils.logger import setup_logging
from api.client import ReqresClient


@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    setup_logging()


@pytest.fixture(scope="session")
def client():
    return ReqresClient()
