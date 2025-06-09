import requests

from api.base_client import BaseClient


class ReqresClient(BaseClient):
    def login(self, email: str, password: str, raise_on_error: bool = True) -> requests.Response:
        data = {"email": email, "password": password}
        return self.post(endpoint="/login", json=data, raise_on_error=raise_on_error)

    def register(self, email: str, password: str, raise_on_error: bool = True) -> requests.Response:
        data = {"email": email, "password": password}
        return self.post(endpoint="/register", json=data, raise_on_error=raise_on_error)

    def get_users(self, page: int = 1, raise_on_error: bool = True) -> requests.Response:
        return self.get(endpoint="/users", params={"page": page}, raise_on_error=raise_on_error)
