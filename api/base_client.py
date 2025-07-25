import requests
from config.config import BASE_URL, API_KEY
import logging
from exceptions.api_exceptions import ApiException, UnauthorizedException, NotFoundException, ServerErrorException


class BaseClient:
    def __init__(self, base_url: str = BASE_URL, api_key: str = API_KEY):
        self.base_url = base_url
        self.headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json"
        }
        self.logger = logging.getLogger(self.__class__.__name__)

    def _make_request(self, method: str, endpoint: str, raise_on_error: bool = True, **kwargs):
        url = f"{self.base_url}{endpoint}"
        if "headers" not in kwargs:
            kwargs["headers"] = self.headers
        else:
            # Объединяем кастомные и дефолтные хедеры
            kwargs["headers"] = {**self.headers, **kwargs["headers"]}

        self.logger.info(f"Request: {method} {url}")
        self.logger.info(f"Request headers: {kwargs.get('headers')}")
        if "json" in kwargs:
            self.logger.info(f"Request JSON body: {kwargs['json']}")
        if "params" in kwargs:
            self.logger.info(f"Request params: {kwargs['params']}")

        response = requests.request(method=method, url=url, **kwargs)

        self.logger.info(f"Response status: {response.status_code}")
        try:
            self.logger.info(f"Response JSON: {response.json()}")
        except ValueError:
            self.logger.info(f"Response text: {response.text}")

        if raise_on_error:
            if response.status_code == 401:
                raise UnauthorizedException("Unauthorized access (401).")
            elif response.status_code == 404:
                raise NotFoundException("Resource not found (404).")
            elif 500 <= response.status_code < 600:
                raise ServerErrorException(f"Server error ({response.status_code}).")
            elif response.status_code >= 400:
                raise ApiException(f"Unexpected error: {response.status_code} - {response.text}")

        return response

    def get(self, endpoint: str, **kwargs):
        return self._make_request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self._make_request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs):
        return self._make_request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self._make_request("DELETE", endpoint, **kwargs)
