from api.base_client import BaseClient


class ReqresClient(BaseClient):
    def login(self, email: str, password: str):
        data = {"email": email, "password": password}
        return self.post(endpoint="/login", json=data)

    def register(self, email: str, password: str):
        data = {"email": email, "password": password}
        return self.post(endpoint="/register", json=data)

    def get_users(self, page: int = 1):
        return self.get(endpoint="/users", params={"page": page})
