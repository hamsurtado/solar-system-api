import pytest

@pytest.mark.skip
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planet")
    response_body = response.get_json()
    
    # Assert
    assert response.status_code == 200
    assert response_body == []

@pytest.mark.skip    
def test_get_one_planet(client):
    # Act
    response = client.get("/planet/1")
    response_body = response.get_json()
    
    #Assert 
    assert response.status_code == 404
    assert response_body is None
    
def test_get_one_planet(client, three_saved_planets):
    # Act
    response = client.get("/planet/1")
    response_body = response.get_json()
    
    # Assert 
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mars",
        "description": "red",
        "has_water": True
    }
