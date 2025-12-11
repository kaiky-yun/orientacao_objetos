def test_register_login_logout_flow(client):
    response = client.post("/register", data={
        "username": "test",
        "email": "test@test.com",
        "password": "123456"
    })
    assert response.status_code in (200, 302)

    response = client.post("/login", data={
        "username": "test",
        "password": "123456"
    })
    assert response.status_code in (200, 302)

    response = client.get("/logout")
    assert response.status_code in (200, 302)
