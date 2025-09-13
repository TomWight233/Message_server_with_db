def test_get_home(web_client):
    response = web_client.get("/hello")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello, world!"
    
def test_get_first_message(web_client):
    post_response = web_client.post("/", data = {"message": "first message"})
    assert post_response.status_code == 302
    
    get_response = web_client.get("/")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "first message"