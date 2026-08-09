def test_create_user(client):
    data = {"email": "test@example.com", "password": "testpassword" }
    response = client.post("/users/", json=data)
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"