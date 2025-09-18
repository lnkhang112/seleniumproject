from api.api_helper import get_user, create_user

def test_get_user_information():
    response = get_user(2)
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert data["data"]["id"] == 2

def test_create_user():
    payload = {"name": "Khang", "job": "Tester"}
    response = create_user(payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Khang"
    assert data["job"] == "Tester"
