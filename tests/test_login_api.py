from models import LoginResponse


def test_successful_login(client):
    response = client.login(email="eve.holt@reqres.in", password="cityslicka")
    assert isinstance(response, LoginResponse)
    assert response.token


def test_login_missing_password(client):
    response = client.login(email="eve.holt@reqres.in", password="", raise_on_error=False)
    assert response.status_code == 400, f"При попытке логина без пароля - вернулся {response.status_code} статус-код"
    assert response.json()["error"] == "Missing password"
