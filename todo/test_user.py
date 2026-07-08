from fastapi.testclient import TestClient

from app.app import app

client = TestClient(app)

def test_get_user():

    response = client.get("/api/user/")

    assert response.status_code == 200

    assert isinstance(response.json() , list)


def test_create_user():

    response = client.post(
        "/api/auth/register",
        json={
            "name": "ashishmaurya",
            "email": "kumarsingh12@gmail.com",
            "password": "ashishmaurya123",
            "confirm_password": "ashishmaurya123"
        }
    )

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200