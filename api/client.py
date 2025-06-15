import requests
from api.base_client import BaseClient
from models import LoginResponse, CreateResponse, GetResponse


class ReqresClient(BaseClient):
    def login(self, email: str, password: str, raise_on_error: bool = True) -> LoginResponse | requests.Response:
        data = {"email": email, "password": password}
        response = self.post(endpoint="/login", json=data, raise_on_error=raise_on_error)

        if raise_on_error:
            return LoginResponse(**response.json())
        return response

    def register(self, email: str, password: str, raise_on_error: bool = True) -> requests.Response:
        data = {"email": email, "password": password}
        return self.post(endpoint="/register", json=data, raise_on_error=raise_on_error)

    def get_users(self, page: int = 1, raise_on_error: bool = True) -> requests.Response:
        return self.get(endpoint="/users", params={"page": page}, raise_on_error=raise_on_error)

    def create_user(self, name: str, job: str, raise_on_error: bool = True) -> CreateResponse | requests.Response:
        data = {"name": name, "job": job}
        response = self.post(endpoint="/users", json=data, raise_on_error=raise_on_error)

        if raise_on_error:
            return CreateResponse(**response.json())
        return response

    def get_user_by_id(self, user_id: int, raise_on_error: bool = True):
        response = self.get(endpoint=f"/users/{user_id}", raise_on_error=raise_on_error)

        if raise_on_error:
            return GetResponse(**response.json())
        return response
