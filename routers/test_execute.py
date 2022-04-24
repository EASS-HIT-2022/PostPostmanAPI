from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_get_all_monitor_executions():
    response = client.get("/executor/626452dd8fca76af5f088bfb")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["_id"] != None
    
def test_execute_monitor_by_id():
    pass
    #response = client.post("/executor/execute/626452dd8fca76af5f088bfb")
    # assert response.status_code == 200
    # assert response.json()["acknowledged"] == True
    # assert response.json()["inserted_id"] != None
    
def test_execute_monitor_by_id_inexistent_item():
    response = client.post("/executor/execute/726452dd8fca76af5f088bfb")
    assert response.status_code == 400