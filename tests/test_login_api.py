def test_successful_login(client):
    response = client.login(email="eve.holt@reqres.in", password="cityslicka")
    assert response.status_code == 200, f"При попытке логина - вернулся {response.status_code} статус-код"
    assert "token" in response.json()


def test_login_missing_password(client):
    response = client.login(email="eve.holt@reqres.in", password="")
    assert response.status_code == 400, f"При попытке логина без пароля - вернулся {response.status_code} статус-код"
    assert response.json()["error"] == "Missing password"
