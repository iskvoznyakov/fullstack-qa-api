from datetime import datetime, timedelta, timezone
import pytest
from models import UserUpdatePutResponse
import allure


@pytest.mark.parametrize("user_id, name, job", [(1, "Ivan", "QA Engineer"), (2, "Tatyana", "Analyst")])
@allure.feature("Updating user")
@allure.story("Updating user with a valid ID")
@allure.title("User is updated successfully with valid ID: {user_id}")
@allure.description("Тест проверяет успешное обновление информации о пользователе с валидным ID.")
def test_successful_update_user_by_id_with_put(client, user_id, name, job):
    with allure.step("Выполняем запрос обновления пользователя с валидным ID"):
        response = client.update_user_by_id_with_put(user_id=user_id, name=name, job=job)
    with allure.step("Проверяем, что ответ является экземпляром UpdateResponse"):
        assert isinstance(response, UserUpdatePutResponse)
    with allure.step("Проверяем, что в ответе возвращаются заданные name и job"):
        assert response.name == name, f"Имя не изменилось, вернулось {response.name}"
        assert response.job == job, f"Должность не изменилась, вернулось {response.job}"
    with allure.step("Проверяем, что время обновления находится в пределах разумного диапазона"):
        now = datetime.now(timezone.utc)
        min_expected = now - timedelta(seconds=3)
        max_expected = now + timedelta(seconds=5)
        assert min_expected <= response.updatedAt <= max_expected, (
            f"Ожидали время между {min_expected} и {max_expected}, но получили {response.updatedAt}"
        )


@pytest.mark.parametrize("user_id, name, job",
                         [(-1, "Ivan", "QA Engineer"),
                          (2, '', ''),
                          (1, 2, 3),
                          (4, '!@#$%^&*()', '!@#$%^&*()')])
@pytest.mark.xfail(reason="API incorrectly accepts invalid update payloads and returns success.")
@allure.feature("Updating user")
@allure.story("Updating user with invalid data")
@allure.title("User update should fail with invalid data: {user_id, name, job}")
@allure.description(
    "Нежелательное поведение: API принимает невалидные данные и возвращает успешный ответ вместо ошибки.")
def test_failed_update_user_by_id_with_put(client, user_id, name, job):
    with allure.step("Выполняем запрос обновления пользователя с невалидными данными"):
        response = client.update_user_by_id_with_put(user_id=user_id, name=name, job=job, raise_on_error=False)
    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 400, f"Ожидали 400 статус-код, получили {response.status_code}"
