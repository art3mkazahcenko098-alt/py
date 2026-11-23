from tests.conftest import client

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_register_login_flow():
    email = "student@example.com"
    password = "StrongPass123!"
    response = client.post("/users/register", json={"email": email, "password": password})
    assert response.status_code == 201

    response = client.post("/auth/login", data={"username": email, "password": password})
    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"

def test_login_rate_limited():
    for _ in range(6):
        response = client.post("/auth/login", data={"username": "nobody@example.com", "password": "wrongpass"})
    assert response.status_code == 429
