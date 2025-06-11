from models import LoginResponse
import allure


@allure.feature("Login")
@allure.story("Successful login")
@allure.title("Successful login with valid email and password")
@allure.description("Тест проверяет успешный логин с валидными email и password.")
def test_successful_login(client):
    with allure.step("Выполняем запрос логина с валидными данными"):
        response = client.login(email="eve.holt@reqres.in", password="cityslicka")
    with allure.step("Проверяем, что ответ является экземпляром LoginResponse"):
        assert isinstance(response, LoginResponse)
    with allure.step("Проверяем, что в ответе есть токен"):
        assert response.token


@allure.feature("Login")
@allure.story("Failed login")
@allure.title("Unsuccessful login with valid email and empty password")
@allure.description("Тест проверяет ошибку при попытке логина без пароля.")
def test_login_missing_password(client):
    with allure.step("Выполняем запрос логина без пароля"):
        response = client.login(email="eve.holt@reqres.in", password="", raise_on_error=False)
    with allure.step("Проверяем, что статус код 400"):
        assert response.status_code == 400, f"При попытке логина без пароля - вернулся {response.status_code} статус-код"
    with allure.step("Проверяем, что сообщение об ошибке 'Missing password' присутствует в ответе"):
        assert response.json()["error"] == "Missing password"
