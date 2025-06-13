from models import CreateResponse
import allure


@allure.feature("Creating user")
@allure.story("User creation with valid data")
@allure.title("User is created successfully with valid name and job")
@allure.description("Тест проверяет успешное создание пользователя с валидными name и job.")
def test_successful_create_user(client, user_data):
    name = user_data["name"]
    job = user_data["job"]
    with allure.step("Выполняем запрос создания пользователя с валидными данными"):
        response = client.create_user(name=name, job=job)
    with allure.step("Проверяем, что ответ является экземпляром CreateResponse"):
        assert isinstance(response, CreateResponse)
    with allure.step("Проверяем, что в ответе возвращаются заданные name и job"):
        assert response.name == name, f"Возвращаемое имя: {response.name} не совпадает с пришедшим на вход: {name}"
        assert response.job == job, f"Возвращаемая работа: {response.job} не совпадает с пришедшей на вход: {job}"
    with allure.step("Проверяем, что в ответе есть id и createdAt"):
        assert response.id, "В ответе не возвращается id"
        assert response.createdAt, "В ответе не возвращается createdAt"
