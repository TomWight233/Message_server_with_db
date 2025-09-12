def test_get_home(web_client):
    response = web_client.get("/hello")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello, world!"