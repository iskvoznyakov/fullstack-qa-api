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


@pytest.mark.parametrize("user_id", [9999, 0, -1, 'id'])
@allure.feature("Getting user")
@allure.story("Getting user with an invalid ID")
@allure.title("User is retrieved unsuccessfully with invalid ID: {user_id}")
@allure.description(
    "Тест проверяет возвращение корректной ошибки при запросе информации о пользователе с невалидным ID.")
def test_failed_get_user_by_id(client, user_id):
    with allure.step("Выполняем запрос получения пользователя с невалидным ID"):
        response = client.get_user_by_id(user_id=user_id, raise_on_error=False)
    with allure.step("Проверяем, что статус-код ответа = 404"):
        assert response.status_code == 404, f"Статус-код ответа: {response.status_code}, а не 404"
    with allure.step("Проверяем, что в ответе возвращается пустой JSON"):
        assert response.json() == {}, f"В ответе вернулось: {response.json()}, а не пустой JSON"
