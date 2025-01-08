from fastapi.testclient import TestClient
from ваша_программа import app

client = TestClient(app)

def test_info():
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json() == '111'

def test_predict():
    with open("путь_к_вашему_изображению", "rb") as img_file:
        response = client.post("/predict2", files={"file": img_file})
        assert response.status_code == 200