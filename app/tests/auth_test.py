
# Login

def test_login_success(client):
    response = client.post("/api/login", json={
        "username": "test1000",
        "password": "test1000",
    })
    assert response.status_code == 200
    assert response.json["msg"] == "login success"
    assert response.json["token"] is not None


def test_login_failure(client):
    response = client.post("/api/login", json={
        "username": "test1001",
        "password": "test1001",
    })
    assert response.status_code == 200
    assert response.json["err_msg"] == "wrong credentials"


