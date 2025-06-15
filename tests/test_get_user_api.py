import pytest
from models import GetResponse
import allure


@pytest.mark.parametrize("user_id", [1, 2, 5, 10])
@allure.feature("Getting user")
@allure.story("Getting user with a valid ID")
@allure.title("User is retrieved successfully with valid ID: {user_id}")
@allure.description("Тест проверяет успешное получение информации о пользователе с валидным ID.")
def test_successful_get_user_by_id(client, user_id):
    with allure.step("Выполняем запрос получения пользователя с валидным ID"):
        response = client.get_user_by_id(user_id=user_id)
    with allure.step("Проверяем, что ответ является экземпляром GetResponse"):
        assert isinstance(response, GetResponse)
    with allure.step("Проверяем, что в ответе возвращается заданный ID"):
        assert response.data.id == user_id, f"Возвращаемый ID: {response.data.id} не совпадает с пришедшим на вход: {user_id}"
