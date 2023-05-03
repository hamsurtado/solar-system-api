import pytest

# @pytest.mark.skip
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planet")
    response_body = response.get_json()
    
    # Assert
    assert response.status_code == 200
    assert response_body == []
    
def test_get_one_planet_gets_404(client):
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

def test_get_all_planets(client, three_saved_planets):
    response = client.get("/planet")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == three_saved_planets
   
def test_post_a_planet(client):
    response = client.post("/planet", json={
        "name": "Venus",
        "description": "yellow",
        "has_water": True
    })
    response_body = response.get_json()
    assert response.status_code == 201
    assert response_body == "Planet Venus with id 1 successfully created"
