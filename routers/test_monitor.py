from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_get_all_monitors():
    response = client.get("/monitor")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["_id"] != None
    
def test_get_monitor_by_id():
    response = client.get("/monitor/626452dd8fca76af5f088bfb")
    assert response.status_code == 200
    assert response.json()["_id"] == '626452dd8fca76af5f088bfb'
    
def test_get_monitor_by_id_inexistent_item():
    response = client.get("/monitor/726452dd8fca76af5f088bfb")
    assert response.status_code == 400
    
def test_create_monitor():
    response = client.put(
        "/monitor",
        json={"name": "string",
              "description": "string",
              "collection_url": "string"},
    )
    assert response.status_code == 200
    assert response.json()["acknowledged"] == True
    assert response.json()["inserted_id"] != None

def test_update_monitor():
    pass

def test_update_monitor_inexistent_item():
    pass

def test_delete_monitor():
    pass

def test_delete_monitor_inexistent_item():
    pass



    