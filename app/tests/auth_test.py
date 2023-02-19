""" Authentication Unit Tests """


# Register
def test_register_success(client):
    """ Test Successful Registration """
    response = client.post("/api/register", json={
        "email": "test1000@email.com",
        "username": "test1000",
        "password": "test1000",
    })
    assert response.status_code == 200
    assert response.json["msg"] == "registration success"


def test_register_failure(client):
    """ Test Registration Failure """
    response = client.post("/api/register", json={
        "email": "test1000@email.com",
        "username": "test1000",
        "password": "test1000",
    })
    assert response.status_code == 200
    assert response.json["err_msg"] == "email exists"


# Login
def test_login_success(client):
    """ Test Successful Login """
    response = client.post("/api/login", json={
        "username": "test1000",
        "password": "test1000",
    })
    assert response.status_code == 200
    assert response.json["msg"] == "login success"
    assert response.json["token"] is not None


def test_login_failure(client):
    """ Test Login Failure """
    response = client.post("/api/login", json={
        "username": "test1001",
        "password": "test1001",
    })
    assert response.status_code == 200
    assert response.json["err_msg"] == "wrong credentials"
