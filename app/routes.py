from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, has_water):
        self.id = id
        self.name = name
        self.description = description
        self.has_water = has_water
        
        
planet1 = Planet(35, "Mars", "red", True)
planet2 = Planet(65, "Jupiter", "orange", True)
planet3 = Planet(1, "Earth", "green", True)

planet_list = [planet1, planet2, planet3]

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")

@planet_bp.route("", methods=["GET"])

def get_planets():
    response = []
    for planet in planet_list:
        planet_dict = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "has_water": planet.has_water            
        }
        
    response.append(planet_dict)
    
    return jsonify(response), 200

