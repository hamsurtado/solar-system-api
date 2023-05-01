from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request


# class Planet:
#     def __init__(self, id, name, description, has_water):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.has_water = has_water
        
        
# planet1 = Planet(35, "Mars", "red", True)
# planet2 = Planet(65, "Jupiter", "orange", True)
# planet3 = Planet(1, "Earth", "green", True)

# planet_list = [planet1, planet2, planet3]

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")

@planet_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"], 
                        description=request_body["description"], 
                        has_water=request_body["has_water"])

    db.session.add(new_planet)
    db.session.commit()
    
    return make_response(f"Planet {new_planet.name} with id {new_planet.id} successfully created", 201)

@planet_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(planet.to_dict())
        
    return jsonify(planets_response), 200

@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return {"message": f"invalid id: {planet_id}"}, 400
    
    planet = Planet.query.get_or_404(planet_id)
    
    return planet.to_dict(), 200       
        
@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return {"message": f"invalid id: {planet_id}"}, 400
    
    planet = Planet.query.get_or_404(planet_id)
    request_data = request.get_json()

    planet.name = request_data["name"]
    planet.description = request_data["description"]
    planet.has_water = request_data["has_water"]

    db.session.commit()
    return {"mssg": f"planet {planet_id} successfully updated"}, 200

@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return {"message": f"invalid id: {planet_id}"}, 400
    
    planet = Planet.query.get_or_404(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return {"mssg": f"planet {planet_id} succesfully annihilated"}, 200
    
